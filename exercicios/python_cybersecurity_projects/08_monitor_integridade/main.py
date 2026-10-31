import argparse, hashlib, json
from pathlib import Path

def hash_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(65536), b""): h.update(b)
    return h.hexdigest()

def coletar(pasta):
    return {str(p.relative_to(pasta)): hash_file(p) for p in pasta.rglob("*") if p.is_file() and p.name != "baseline.json"}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("pasta", type=Path)
    p.add_argument("acao", choices=["baseline", "verificar"])
    a = p.parse_args()
    if not a.pasta.is_dir(): p.error("Pasta não encontrada.")
    base = a.pasta / "baseline.json"
    atual = coletar(a.pasta)
    if a.acao == "baseline":
        base.write_text(json.dumps(atual, indent=2))
        print("Linha de base salva.")
    else:
        if not base.exists(): p.error("Execute baseline primeiro.")
        antigo = json.loads(base.read_text())
        for nome in sorted(atual.keys() - antigo.keys()): print("[NOVO]", nome)
        for nome in sorted(antigo.keys() - atual.keys()): print("[REMOVIDO]", nome)
        for nome in sorted(atual.keys() & antigo.keys()):
            if atual[nome] != antigo[nome]: print("[ALTERADO]", nome)
