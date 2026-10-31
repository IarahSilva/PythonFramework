import argparse, hashlib, zipfile
from datetime import datetime
from pathlib import Path

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for bloco in iter(lambda: f.read(65536), b""): h.update(bloco)
    return h.hexdigest()

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("origem", type=Path)
    p.add_argument("--destino", type=Path, default=Path(f"backup_{datetime.now():%Y%m%d_%H%M%S}.zip"))
    a = p.parse_args()
    if not a.origem.is_dir(): p.error("Pasta de origem não encontrada.")
    a.destino.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(a.destino, "w", zipfile.ZIP_DEFLATED) as z:
        for item in a.origem.rglob("*"):
            if item.is_file() and item.resolve() != a.destino.resolve():
                z.write(item, item.relative_to(a.origem))
    digest = sha256(a.destino)
    a.destino.with_suffix(".zip.sha256").write_text(digest + "  " + a.destino.name + "\n")
    print("Backup:", a.destino)
    print("SHA-256:", digest)
