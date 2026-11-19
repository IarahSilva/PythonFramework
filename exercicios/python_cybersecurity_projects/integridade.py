import hashlib
import json
import os

BANCO = "hashes.json"


def gerar_hash(caminho):
    sha256 = hashlib.sha256()

    with open(caminho, "rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(4096), b""):
            sha256.update(bloco)

    return sha256.hexdigest()


def carregar_banco():
    if os.path.exists(BANCO):
        with open(BANCO, "r") as f:
            return json.load(f)

    return {}


def salvar_banco(dados):
    with open(BANCO, "w") as f:
        json.dump(dados, f, indent=4)


def verificar(caminho):
    if not os.path.isfile(caminho):
        print("Arquivo inexistente.")
        return

    banco = carregar_banco()
    atual = gerar_hash(caminho)

    if caminho not in banco:
        banco[caminho] = atual
        salvar_banco(banco)
        print("Hash inicial registrado.")

    elif banco[caminho] == atual:
        print("INTEGRIDADE CONFIRMADA.")

    else:
        print("ALERTA: ARQUIVO MODIFICADO!")
        print("Hash anterior:", banco[caminho])
        print("Hash atual:", atual)


if __name__ == "__main__":
    arquivo = input("Caminho do arquivo: ")
    verificar(arquivo)