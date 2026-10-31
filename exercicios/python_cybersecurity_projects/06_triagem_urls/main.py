import argparse, ipaddress
from urllib.parse import urlparse

ENCURTADORES = {"bit.ly", "tinyurl.com", "t.co", "is.gd"}

def analisar(url):
    alvo = url if "://" in url else "https://" + url
    partes = urlparse(alvo)
    host = partes.hostname or ""
    alertas = []
    if partes.scheme != "https": alertas.append("Não usa HTTPS.")
    if "@" in partes.netloc: alertas.append("Contém @ na autoridade.")
    if host.lower() in ENCURTADORES: alertas.append("Link encurtado: destino oculto.")
    try:
        ipaddress.ip_address(host)
        alertas.append("Usa endereço IP diretamente.")
    except ValueError: pass
    if len(url) > 150: alertas.append("URL muito longa.")
    return alertas

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("url")
    a = p.parse_args()
    resultados = analisar(a.url)
    print("\n".join("- " + x for x in resultados) if resultados else "Nenhum sinal simples encontrado.")
    print("A ausência de alertas não garante que o endereço seja seguro.")
