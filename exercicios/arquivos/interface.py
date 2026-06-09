from os import system as lt
lt("cls")

def menu(user, age):
    print(f"Bem vindo {user}.")
    print(f"Você tem {age} anos.")
    print("Seleciona uma opção abaiaxo:")
    print("1 - Recepção")
    print("2 - Secretaria")
    print("3 - Sala de Aula")
    print("4 - Diretoria")
    print("5 - Sair")
    opcao = input("-> ")
    return opcao

def escolha(sel):
    match sel:
        case "1":
            print("Você pode ir até a recepção.")
        case "2":
            print("Você pode ir até a secretaria.")
        case "3":
            print("Você pode ir até para a sala de aula.")
        case "4":
            print("Você pode ir até a diretoria.")
        case "5":
            print("Você pode ir embora.")
        case _:
            print("Escolha uma opção válida!!!")
    return None

