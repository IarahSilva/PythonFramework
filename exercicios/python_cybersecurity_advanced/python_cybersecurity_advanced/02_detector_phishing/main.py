import argparse
import email
import re
from email import policy
from pathlib import Path
from urllib.parse import urlparse

URL_RE = re.compile(r"""https?://[^\s<>"')\]]+""", re.IGNORECASE)
SHORTENERS = {"bit.ly", "tinyurl.com", "t.co", "is.gd", "ow.ly", "buff.ly"}
SUSPICIOUS_WORDS = {"urgente", "urgent", "verify", "verifique", "suspensa",
                    "suspended", "senha", "password", "pagamento", "payment",
                    "clique", "click", "atualize", "update"}

def extract_urls(text):
    return sorted(set(u.rstrip(".,;:!?") for u in URL_RE.findall(text)))

def score_url(url):
    reasons = []
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    if parsed.scheme != "https":
        reasons.append("URL não usa HTTPS")
    if parsed.username or parsed.password:
        reasons.append("URL contém credenciais embutidas")
    if host in SHORTENERS:
        reasons.append("Serviço de encurtamento de URL")
    if host.startswith("xn--") or ".xn--" in host:
        reasons.append("Domínio internacionalizado (Punycode)")
    if re.search(r"\d+\.\d+\.\d+\.\d+", host):
        reasons.append("Host parece ser um endereço IPv4")
    if len(url) > 100:
        reasons.append("URL muito longa")
    if host.count("-") >= 3:
        reasons.append("Muitos hífens no domínio")
    return reasons

def analyze_message(sender, subject, body):
    text = f"{subject}\n{body}".lower()
    findings = []
    for word in sorted(SUSPICIOUS_WORDS):
        if word in text:
            findings.append(f"Linguagem de urgência/solicitação: '{word}'")
    urls = extract_urls(body)
    url_findings = []
    for url in urls:
        reasons = score_url(url)
        if reasons:
            url_findings.append((url, reasons))
    if sender and "@" not in sender:
        findings.append("Campo de remetente não parece conter um endereço de e-mail")
    score = len(findings) + sum(len(r) for _, r in url_findings)
    return score, findings, url_findings, urls

def read_eml(path):
    msg = email.message_from_binary_file(open(path, "rb"), policy=policy.default)
    sender = str(msg.get("From", ""))
    subject = str(msg.get("Subject", ""))
    parts = []
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                try: parts.append(part.get_content())
                except (KeyError, UnicodeDecodeError): pass
    else:
        try: parts.append(msg.get_content())
        except (KeyError, UnicodeDecodeError): pass
    return sender, subject, "\n".join(map(str, parts))

def main():
    parser = argparse.ArgumentParser(description="Analisador heurístico de e-mails e URLs.")
    parser.add_argument("file", help="Arquivo .eml ou .txt")
    args = parser.parse_args()
    path = Path(args.file)
    if not path.is_file():
        raise SystemExit("Arquivo não encontrado.")
    if path.suffix.lower() == ".eml":
        sender, subject, body = read_eml(path)
    else:
        body = path.read_text(encoding="utf-8", errors="replace")
        sender, subject = "", ""
    score, findings, url_findings, urls = analyze_message(sender, subject, body)
    print("=== ANÁLISE DE PHISHING (HEURÍSTICA) ===")
    print("Remetente:", sender or "(não informado)")
    print("Assunto:", subject or "(não informado)")
    print("Pontuação indicativa:", score)
    print("\nSinais encontrados:")
    for item in findings: print("-", item)
    for url, reasons in url_findings:
        print(f"\nURL: {url}")
        for reason in reasons: print(" -", reason)
    if not findings and not url_findings:
        print("Nenhum sinal heurístico identificado.")
    print("\nURLs extraídas:")
    for url in urls: print("-", url)
    print("\nResultado não conclusivo: confirme por outros meios; não abra links suspeitos.")

if __name__ == "__main__":
    main()
