def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    print(f"Sua média foi: {media}")
    return media

n1 = float(input("Insira sua primeira nota: "))
n2 = float(input("Insira sua segunda nota: "))
calcular_media(n1, n2)