import math
import string


def analisar(senha):
    alfabeto = 0

    if any(c in string.ascii_lowercase for c in senha):
        alfabeto += 26

    if any(c in string.ascii_uppercase for c in senha):
        alfabeto += 26

    if any(c in string.digits for c in senha):
        alfabeto += 10

    if any(c in string.punctuation for c in senha):
        alfabeto += len(string.punctuation)

    if alfabeto == 0:
        return 0

    entropia = len(senha) * math.log2(alfabeto)

    return entropia


senha = input("Digite uma senha: ")

bits = analisar(senha)

print(f"Entropia estimada: {bits:.2f} bits")

if bits < 40:
    print("Segurança estimada: baixa")
elif bits < 60:
    print("Segurança estimada: moderada")
else:
    print("Segurança estimada: alta")