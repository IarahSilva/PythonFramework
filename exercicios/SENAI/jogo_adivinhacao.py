import random

numero = random.randint(1, 10)

tentativa = int(input("Adivinhe o número de 1 a 10: "))

if tentativa == numero:
    print("Você acertou!")
else:
    print("Você errou! O número era", numero)

#================================
#       JOGO DE ADIVINHAÇÃO
#================================

#Pensei em um número de 1 a 100!

#Digite seu palpite: 50

#O número é maior!

#Digite seu palpite: 75

#O número é menor!

#Digite seu palpite: 63

#PARABÉNS! Você acertou!

#Tentativas: 3