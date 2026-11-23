class Perfil():
    def __init__(self, idade:int):
        if idade > 18:
            self.status = "Adulto"
        else:
            self.status = "Menor"

cliente = Perfil(19)
print(f"O cliente é {cliente.status}.")


