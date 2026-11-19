import json
import os
from cryptography.fernet import Fernet

ARQUIVO_CHAVE = "secret.key"
ARQUIVO_DADOS = "senhas.enc"


def carregar_chave():
    if not os.path.exists(ARQUIVO_CHAVE):
        chave = Fernet.generate_key()
        with open(ARQUIVO_CHAVE, "wb") as f:
            f.write(chave)

    with open(ARQUIVO_CHAVE, "rb") as f:
        return Fernet(f.read())


def carregar_senhas(fernet):
    if not os.path.exists(ARQUIVO_DADOS):
        return {}

    with open(ARQUIVO_DADOS, "rb") as f:
        dados = f.read()

    return json.loads(fernet.decrypt(dados))


def salvar_senhas(fernet, senhas):
    dados = json.dumps(senhas).encode()
    criptografado = fernet.encrypt(dados)

    with open(ARQUIVO_DADOS, "wb") as f:
        f.write(criptografado)


def main():
    fernet = carregar_chave()
    senhas = carregar_senhas(fernet)

    while True:
        print("\n1 - Adicionar senha")
        print("2 - Consultar senha")
        print("3 - Listar serviços")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            servico = input("Serviço: ")
            usuario = input("Usuário: ")
            senha = input("Senha: ")

            senhas[servico] = {
                "usuario": usuario,
                "senha": senha
            }

            salvar_senhas(fernet, senhas)
            print("Credencial armazenada!")

        elif opcao == "2":
            servico = input("Serviço: ")
            registro = senhas.get(servico)

            if registro:
                print("Usuário:", registro["usuario"])
                print("Senha:", registro["senha"])
            else:
                print("Serviço não encontrado.")

        elif opcao == "3":
            for servico in senhas:
                print("-", servico)

        elif opcao == "0":
            break


if __name__ == "__main__":
    main()

//pip install cryptography