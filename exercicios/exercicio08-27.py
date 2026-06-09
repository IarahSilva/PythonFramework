frase_antiga = input("Insira uma frase: ")
nova_frase = " "
vogais = "aeiouAEIOU"

for i in frase_antiga:
    
    if i not in vogais:
        nova_frase = nova_frase + i
        print(nova_frase)


