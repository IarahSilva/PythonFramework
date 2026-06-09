def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in frase: 
        if letra in vogais:
            contador += 1
        return contador
    
frase = "Ola Mundo!"
total_vogais = contar_vogais(frase)
print(f"A frase atual contem {total_vogais} vogais!")