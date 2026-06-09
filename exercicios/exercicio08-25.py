contador_letra = 0
frase = input("Insira uma frase: ")
letra = input("Insira uma letra: ")

for i in frase:
    if i in letra:
        contador_letra += 1

print(f"\nA frase '{frase}' tem {contador_letra} letras presentes!")
