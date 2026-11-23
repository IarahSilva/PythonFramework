def Lambda(num):
    mult = num * 5
    return mult

num = float(input("Insira o número que será multiplicado: "))
resultado = Lambda(num)
print(f"O valor resultante é: {resultado}")