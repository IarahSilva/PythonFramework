class Retangulo():
    def __init__(self, base:float, altura:float):
        self.base = base
        self.altura = altura
        self.area = base * altura
        
ret = Retangulo(10, 5)
print(f"A area calculada foi: {ret.area}.")

