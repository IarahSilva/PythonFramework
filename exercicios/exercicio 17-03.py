class Planeta():
    def __init__(self, formato:str):
        self.formato = formato
planeta_forma = Planeta("Esférico")
print(f"O planeta possui uma forma: {planeta_forma.formato}")
