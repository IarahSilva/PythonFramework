# Importa a biblioteca re para trabalhar com expressões regulares
import re

# Função responsável por analisar a senha
def analisar_senha(senha):

    # Dicionário que verifica os critérios de segurança
    criterios = {
        # Verifica se a senha possui pelo menos 8 caracteres
        "8 caracteres": len(senha) >= 8,

        # Verifica se existe pelo menos uma letra maiúscula
        "Letra maiúscula": bool(re.search(r"[A-Z]", senha)),

        # Verifica se existe pelo menos uma letra minúscula
        "Letra minúscula": bool(re.search(r"[a-z]", senha)),

        # Verifica se existe pelo menos um número
        "Número": bool(re.search(r"\d", senha)),

        # Verifica se existe algum caractere especial
        "Caractere especial": bool(re.search(r"[^a-zA-Z0-9]", senha))
    }

    # Percorre os critérios e mostra se foram atendidos
    for criterio, resultado in criterios.items():
        print(f"{criterio}: {'OK' if resultado else 'FALHOU'}")

    # Soma os critérios que foram atendidos
    pontos = sum(criterios.values())

    # Exibe a pontuação final
    print(f"\nPontuação: {pontos}/5")


# Solicita uma senha ao usuário
senha = input("Digite uma senha: ")

# Chama a função para analisar a senha digitada
analisar_senha(senha)