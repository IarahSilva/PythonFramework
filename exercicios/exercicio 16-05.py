def saudacao(cidade: str, nome: str):
    print(f"Olá {nome}, Seja Bem-Vindo a cidade de {cidade}!")
    return "Aproveite sua Viagem!"

nome = input("Insira seu nome: ")
cidade = input("Insira o nome de sua cidade: ")

saudacaoPronta = saudacao(cidade=cidade, nome=nome)
print(saudacaoPronta)