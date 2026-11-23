import hashlib

def calcular_hash(caminho):
    sha256 = hashlib.sha256()

    with open(caminho, "rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(4096), b""):
            sha256.update(bloco)

    return sha256.hexdigest()


arquivo = "documento.txt"

hash_original = calcular_hash(arquivo)

input("Altere o arquivo e pressione ENTER...")

hash_atual = calcular_hash(arquivo)

if hash_original != hash_atual:
    print("ALERTA: Arquivo modificado!")
else:
    print("Nenhuma alteração detectada.")