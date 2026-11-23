class Bicicleta():
    def __init__(self, cor:str, aro:int):
        self.cor = cor
        self.aro = aro

minha_bike = Bicicleta("Azul", 29)
print(f"A bike possui uma cor: {minha_bike.cor}, e um aro de: {minha_bike.aro}")