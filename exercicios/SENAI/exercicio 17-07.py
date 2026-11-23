class Herói():
    def __init__(self, nome:str, poder:str):
        self.nome = nome
        self.poder = poder
    
heroi1 = Herói("SuperMan", "Voar")
print(f"O {heroi1.nome} possui o poder de {heroi1.poder}!")