def calcula_imc(alt, peso):
    imc = peso / (alt**2)
    return imc

def classificacao(resultado):
    if resultado < 18.5:
        print("Abaixo do peso!")
    elif resultado >= 18.5 and resultado < 24.9:
        print("Peso Normal!")
    elif resultado >= 25 and resultado < 29.9:
        print("Sobrepeso!")
    elif resultado >= 30:
        print("Sobrepeso!")
    else:
        print("Classificação não identificada!")

alt = float(input("Informe sua altura em metros: "))
peso = float(input("Informe seu peso em kg: "))

resultado = calcula_imc(alt, peso)
print(f"Possui um imc de: {resultado}")

clas = classificacao(resultado)
print(f"Sua classificação: {clas}")
