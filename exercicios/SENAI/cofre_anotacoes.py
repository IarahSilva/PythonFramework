def salvar_anotacao():
    texto = input("Digite sua anotação: ")

    with open("anotacoes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(texto + "\n")

    print("Anotação salva!")

salvar_anotacao()

#================================
#       COFRE DE ANOTAÇÕES
#================================

#1 - Criar anotação
#2 - Visualizar anotações
#3 - Sair

#Escolha: 1

#Digite sua anotação:
#Estudar Python e Segurança da Informação.

#Anotação salva com sucesso!

#Escolha: 2

#SUAS ANOTAÇÕES:

#1. Estudar Python e Segurança da Informação.

