def maior_numero(num1, num2):
    if num1 > num2:
        return print(f"O número maior é o {num1}!")
    elif num2 > num1:
        return print(f"O número maior é o {num2}!")
    elif num1 == num2:
        return print("São Iguais!")
    else:
        print("Numéro não identificado!")

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
maior_numero(num1, num2)