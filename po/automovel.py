import time
from os import system as lt
lt("cls")

class Automovel:
    # Atributos
    def __init__(self, ano_fabricacao, modelo, cor, potencia_motor, placa, tipo, marca):
        self.ano_fabricacao = ano_fabricacao
        self.modelo = modelo
        self.cor = cor
        self.potencia_motor = potencia_motor
        self.placa = placa
        self.tipo = tipo
        self.marca = marca
        self.velocidade = 0
        self.ligado = False
    
    # Métodos
    def ligar(self):
        if self.ligado == False:
            self.ligado = True
            return print(f"O carro está ligado")

    def desligar(self):
        if self.ligado == True:
            self.ligado = False
            return print(f"O carro está desligado")

    def acelerar(self):
        if self.velocidade < 110:
            self.velocidade += 5
            return print(f"A velocidade é {self.velocidade} km/h.")
        else:
            return print("Ligue o carro para freiar-lo!")

    def freiar(self):
        if self.velocidade > 0:
            self.velocidade -= 5
        return print(f"Carro desligando em...{self.velocidade} km/h.")

    def buzinar(self):
        if self.ligado == False:
            self.ligado = True
        return print("BIIIIIIIIIIIIII")

    def ligar_farol(self):
        pass

    def dar_re(self):
        pass

    def virar_direita(self):
        pass

    def virar_esquerda(self):
        pass

    def dar_seta(self):
        pass

def menu():
    print("Escolha uma opção abaixo:")
    print("1 - Ligar carro.")
    print("2 - Desigar carro.")
    print("3 - Acelerar.")
    print("4 - Freiar.")
    print("5 - Buzinar.")

carro1 = Automovel(2010, "206", "Vermelho", 1.0, "AAA5678", "Passeio", "Peugeot")

while True:
    lt("cls")
    menu()
    opcao = input("-> ")
    if opcao == "1":
        carro1.ligar()
    elif opcao == "2":
        carro1.desligar()
    elif opcao == "3":
        carro1.acelerar()
    elif opcao == "4":
        carro1.freiar()
    elif opcao == "5":
        carro1.buzinar()
    else:
        print("Escolha uma opção válida.")
    time.sleep(1.1)


print()
