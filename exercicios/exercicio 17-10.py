class Robo():
    def __init__(self):
        self.bateria = 100

    def trabalhar(self):
        self.bateria -= 15
        print(f"Limpando bateria restante {self.bateria}%...")

robo = Robo()
robo.trabalhar()

