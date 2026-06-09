def geral_ids(limite: int):
    contador = 1
    while contador <= limite:
        yield contador
        contador = contador + 1

for numero in geral_ids(3):
    print(f"ID Gerado: {numero}")
