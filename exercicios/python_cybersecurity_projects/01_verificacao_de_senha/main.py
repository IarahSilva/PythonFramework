import re
import getpass

def avaliar(senha):
    score = sum(bool(re.search(p, senha)) for p in [r"[a-z]", r"[A-Z]", r"\d", r"[^A-Za-z0-9]"])
    score += 1 if len(senha) >= 12 else 0
    dicas = []
    if len(senha) < 12: dicas.append("Use pelo menos 12 caracteres.")
    if not re.search(r"[A-Z]", senha): dicas.append("Adicione letras maiúsculas.")
    if not re.search(r"[a-z]", senha): dicas.append("Adicione letras minúsculas.")
    if not re.search(r"\d", senha): dicas.append("Adicione números.")
    if not re.search(r"[^A-Za-z0-9]", senha): dicas.append("Adicione símbolos.")
    return score, dicas

if __name__ == "__main__":
    senha = getpass.getpass("Senha (não será armazenada): ")
    score, dicas = avaliar(senha)
    print("Classificação:", "Fraca" if score <= 2 else "Moderada" if score <= 4 else "Forte")
    for dica in dicas: print("-", dica)