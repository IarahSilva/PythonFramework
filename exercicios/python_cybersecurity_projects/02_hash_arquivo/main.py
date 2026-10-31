import argparse, hashlib
from pathlib import Path

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for bloco in iter(lambda: f.read(65536), b""): h.update(bloco)
    return h.hexdigest()

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("arquivo")
    p.add_argument("--esperado")
    a = p.parse_args()
    arquivo = Path(a.arquivo)
    if not arquivo.is_file(): p.error("Arquivo não encontrado.")
    atual = sha256(arquivo)
    print("SHA-256:", atual)
    if a.esperado: print("Integridade:", "OK" if atual.lower() == a.esperado.lower() else "DIVERGENTE")
