def salvar_anotacao():
    texto = input("Digite sua anotação: ")

    with open("anotacoes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(texto + "\n")

    print("Anotação salva!")

salvar_anotacao()

