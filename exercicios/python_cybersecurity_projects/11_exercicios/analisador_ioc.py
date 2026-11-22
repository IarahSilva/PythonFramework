import hashlib
import json
import os

BASE_IOC = {
    # Hashes fictícios para demonstração.
    "0000000000000000000000000000000000000000000000000000000000000000":
        "Indicador de teste A",

    "1111111111111111111111111111111111111111111111111111111111111111":
        "Indicador de teste B"
}


def gerar_hash(caminho):
    sha = hashlib.sha256()

    with open(caminho, "rb") as arquivo:
        for bloco in iter(
            lambda: arquivo.read(4096), b""
        ):
            sha.update(bloco)

    return sha.hexdigest()


def analisar(caminho):
    if not os.path.isfile(caminho):
        print("Arquivo não encontrado.")
        return

    hash_arquivo = gerar_hash(caminho)

    print("Arquivo:", caminho)
    print("SHA-256:", hash_arquivo)

    if hash_arquivo in BASE_IOC:
        print("[ALERTA] Indicador encontrado!")
        print("Descrição:", BASE_IOC[hash_arquivo])
    else:
        print("[INFO] Hash não encontrado na base local.")


if __name__ == "__main__":
    arquivo = input("Arquivo para analisar: ")
    analisar(arquivo)

#Terminal:
#Arquivo: teste.txt
#SHA-256: 3a7bd3e2360a...

#[INFO] Hash não encontrado na base local.