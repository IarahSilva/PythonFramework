senha = input("Digite sua senha: ")

if len(senha) < 6:
    print("Senha fraca")
elif len(senha) < 10:
    print("Senha média")
else:
    print("Senha forte")