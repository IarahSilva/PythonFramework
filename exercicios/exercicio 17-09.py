class Cachorro():
    def __init__(self, nome:str):
        self.nome = nome

ativar_latir = Cachorro("Tótó")
print(f"{ativar_latir.nome} diz: AU AU!!")
