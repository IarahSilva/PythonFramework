import interface
import calculos


while True:
    interface.limpar()
    resltado, num1, num2, num3 = calcularsoma(22, 30)
    nome = input("Por favor, digite seu nome: ")
    idade = int(input("Digite a sua idade: "))
    op = interface.menu(nome, idade)
    interface.escolha(op)


