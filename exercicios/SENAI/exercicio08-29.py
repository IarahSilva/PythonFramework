frase_digitada = input("Insira uma frase: ")
contador_letras = 0
soma = 0
consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

for letra in frase_digitada:
    
    if letra in consoantes:
     soma = contador_letras =+ 1 
     print(soma)

