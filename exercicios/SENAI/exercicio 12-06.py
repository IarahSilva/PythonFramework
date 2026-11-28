
# Cria um dicionário contendo países e suas respectivas capitais
capitais = {
    "Brasil": "Brasília",
    "Estados Unidos": "Washington",
    "Reino Unido": "Londres",
    "França": "Paris",
    "Alemanha": "Berlim",
    "Itália": "Roma",
    "Japão": "Tóquio",
    "China": "Pequim",
    "Rússia": "Moscou",
    "Austrália": "Canberra"
}


# Cria um laço infinito para solicitar um país ao usuário
while True:

    # Solicita que o usuário digite o nome de um país
    capital_inserida = input("Insira o nome do país selecionado: ")

    try:
        # Busca no dicionário a capital correspondente ao país informado
        capital = capitais[capital_inserida]

        # Exibe o país selecionado
        print(f"Opção {capital_inserida} selecionada...")

        # Encerra o laço quando encontra o país
        break

    except KeyError:
        # Executa quando o país não existe no dicionário
        print("Opção não localizada...Tente Novamente.")
