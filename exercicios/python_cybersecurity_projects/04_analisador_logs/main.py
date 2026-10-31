import argparse, re
from collections import Counter
from pathlib import Path

PADRAO = re.compile(r"Failed password for (?:invalid user )?\S+ from ([\d.]+)", re.I)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("arquivo", nargs="?", default="exemplo.log")
    p.add_argument("--limite", type=int, default=1)
    a = p.parse_args()
    arquivo = Path(a.arquivo)
    if not arquivo.is_file(): p.error("Arquivo não encontrado.")
    contagem = Counter()
    for linha in arquivo.read_text(errors="replace").splitlines():
        m = PADRAO.search(linha)
        if m: contagem[m.group(1)] += 1
    print("Falhas por IP:")
    for ip, qtd in contagem.most_common():
        if qtd >= a.limite: print(f"{ip}: {qtd}")
    if not contagem: print("Nenhuma falha reconhecida.")
