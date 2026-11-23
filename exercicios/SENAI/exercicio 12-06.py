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

while True:
 capital_inserida = input("Insira o nome do país selecionado: ")
 try:
    capital = capitais[capital_inserida]
    print(f"Opção {capital_inserida} selecionada...")
    break
 except KeyError:
   print("Opção não localizada...Tente Novamente.")