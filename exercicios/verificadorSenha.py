import re

def analisar_senha(senha):
    criterios = {
        "8 caracteres": len(senha) >= 8,
        "Letra maiúscula": bool(re.search(r"[A-Z]", senha)),
        "Letra minúscula": bool(re.search(r"[a-z]", senha)),
        "Número": bool(re.search(r"\d", senha)),
        "Caractere especial": bool(re.search(r"[^a-zA-Z0-9]", senha))
    }

    for criterio, resultado in criterios.items():
        print(f"{criterio}: {'OK' if resultado else 'FALHOU'}")

    pontos = sum(criterios.values())

    print(f"\nPontuação: {pontos}/5")


senha = input("Digite uma senha: ")
analisar_senha(senha)