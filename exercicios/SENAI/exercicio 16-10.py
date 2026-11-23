def divisaoNumeros(num1: int, num2: int) -> int:
   if(num1 and num2 != 0):
    div = num1 / num2
    return print(f"A divisão final foi de: {div}")
   elif(num1 and num2 == 0):
     return print("A divisão não pode ser feita por 0!")

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
