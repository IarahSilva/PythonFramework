from time import sleep as temp
from os import system as limptela
limptela('cls')

def menu(user, age):
 print(f"Bem-Vindo {user} ao SENAI!\nVocê possui {age} anos!\nSelecione uma opção abaixo: ")
 print("1- Recepção\n2- Secrtária\n3- Sala de aula\n4- Diretoria\n5- Sair")
 opcao = input("-> ")
 return opcao

def escolha(sel):
   match sel:
    case "1":
         print("Voce pode ir para a recepção!")
    case "2":
         print("Voce pode ir para a secretária!")
         
    case "3":
         print("Voce pode ir para a sala de aula!")
         
    case "4":
         print("Voce pode ir para a diretoria!")
         
    case "5":
         print("Voce pode ir para a sair!")
    case _:
        print("Opção inválida!")
         
         


while True:
    nome = input("Insira seu nome: ")
    idade = int(input("Informe a sua idade: "))
    op = menu(nome, idade)
    escolha(op)

