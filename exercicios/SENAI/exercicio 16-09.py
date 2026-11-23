def soma_protegida(num1: int, num2: int) -> int:
    if(num1 and num2 >= 0):
        soma = num1 + num2
        return print(f"A soma final foi: {soma}")
    elif(num1 and num2 < 0):
       return print("Número inválido!")
    
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

