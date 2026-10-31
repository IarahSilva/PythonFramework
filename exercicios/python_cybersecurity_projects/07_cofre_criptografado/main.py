import argparse
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

KEY, DATA = Path("chave.key"), Path("nota.enc")

def carregar_chave():
    if not KEY.exists():
        KEY.write_bytes(Fernet.generate_key())
        try: KEY.chmod(0o600)
        except OSError: pass
        print("Chave criada. Guarde-a: sem ela, não recupera os dados.")
    return Fernet(KEY.read_bytes())

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("acao", choices=["gravar", "ler"])
    p.add_argument("--texto")
    a = p.parse_args()
    f = carregar_chave()
    if a.acao == "gravar":
        if a.texto is None: p.error("Informe --texto.")
        DATA.write_bytes(f.encrypt(a.texto.encode()))
        print("Nota criptografada.")
    else:
        if not DATA.exists(): p.error("Nota ainda não existe.")
        try: print(f.decrypt(DATA.read_bytes()).decode())
        except InvalidToken: p.error("Chave inválida ou arquivo alterado.")
