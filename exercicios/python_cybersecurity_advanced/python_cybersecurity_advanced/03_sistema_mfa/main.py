import argparse
import getpass
import hashlib
import json
import os
import secrets
from pathlib import Path

import pyotp

DATA = Path("mfa_user.json")
SALT_FILE = Path("password_salt.bin")

def derive_password(password, salt):
    # PBKDF2-HMAC-SHA256 com 600 mil iterações para demonstração.
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 600_000)

def setup(username):
    if DATA.exists():
        raise SystemExit("Usuário já configurado. Remova os arquivos locais para reiniciar o laboratório.")
    password = getpass.getpass("Crie uma senha: ")
    if len(password) < 12:
        raise SystemExit("Use pelo menos 12 caracteres.")
    salt = secrets.token_bytes(16)
    password_hash = derive_password(password, salt)
    secret = pyotp.random_base32()
    record = {
        "username": username,
        "password_hash": password_hash.hex(),
        "totp_secret": secret
    }
    DATA.write_text(json.dumps(record, indent=2), encoding="utf-8")
    SALT_FILE.write_bytes(salt)
    uri = pyotp.TOTP(secret).provisioning_uri(name=username, issuer_name="Python MFA Lab")
    print("\nConta criada.")
    print("Segredo TOTP (guarde em local seguro):", secret)
    try:
        import qrcode
        img = qrcode.make(uri)
        img.save("mfa_qr.png")
        print("QR Code salvo em mfa_qr.png; importe em um autenticador compatível.")
    except Exception:
        print("URI para configurar autenticador:", uri)

def login():
    if not DATA.exists() or not SALT_FILE.exists():
        raise SystemExit("Configure primeiro: python main.py setup --user nome")
    record = json.loads(DATA.read_text(encoding="utf-8"))
    salt = SALT_FILE.read_bytes()
    password = getpass.getpass("Senha: ")
    candidate = derive_password(password, salt).hex()
    if not secrets.compare_digest(candidate, record["password_hash"]):
        print("Credenciais inválidas.")
        return
    code = input("Código de 6 dígitos do autenticador: ").strip()
    totp = pyotp.TOTP(record["totp_secret"])
    if totp.verify(code, valid_window=1):
        print(f"Acesso autorizado. Bem-vindo, {record['username']}!")
    else:
        print("Código MFA inválido ou expirado.")

def main():
    parser = argparse.ArgumentParser(description="MFA TOTP educacional.")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("setup")
    p.add_argument("--user", required=True)
    sub.add_parser("login")
    args = parser.parse_args()
    if args.command == "setup": setup(args.user)
    else: login()

if __name__ == "__main__":
    main()
