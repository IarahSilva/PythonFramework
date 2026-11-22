from cryptography.fernet import Fernet
import os

CHAVE = "chave.key"


def obter_chave():
    if not os.path.exists(CHAVE):
        chave = Fernet.generate_key()

        with open(CHAVE, "wb") as f:
            f.write(chave)

    with open(CHAVE, "rb") as f:
        return Fernet(f.read())


def criptografar(caminho, fernet):
    with open(caminho, "rb") as f:
        dados = f.read()

    resultado = fernet.encrypt(dados)

    with open(caminho + ".enc", "wb") as f:
        f.write(resultado)

    print("Arquivo criptografado!")


def descriptografar(caminho, fernet):
    with open(caminho, "rb") as f:
        dados = f.read()

    resultado = fernet.decrypt(dados)

    destino = caminho.removesuffix(".enc") + ".dec"

    with open(destino, "wb") as f:
        f.write(resultado)

    print("Arquivo recuperado:", destino)


if __name__ == "__main__":
    fernet = obter_chave()

    print("1 - Criptografar")
    print("2 - Descriptografar")

    opcao = input("Escolha: ")
    caminho = input("Arquivo: ")

    if opcao == "1":
        criptografar(caminho, fernet)

    elif opcao == "2":
        descriptografar(caminho, fernet)

//1 - Criptografar
//2 - Descriptografar

//Escolha: 1
//Arquivo: documento.txt

//Arquivo criptografado!