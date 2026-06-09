from os import system as lt
lt("cls")

class Pokemon:
    def __init__(self, nome, tipo, ataque, defesa, agilidade):
     self.nome = nome
     self.tipo = tipo
     self.ataque = ataque
     self.defesa = defesa
     self.agilidade = agilidade

player1 = Pokemon("Pikachu", "Eletrico", 55, 50, 50)
player2 = Pokemon("Pikachu", "Eletrico", 55, 50, 50)
