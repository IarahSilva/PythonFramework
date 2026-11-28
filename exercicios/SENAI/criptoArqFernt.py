
# Importa a classe Fernet para realizar a criptografia
from cryptography.fernet import Fernet


# Gera uma chave de criptografia aleatória
chave = Fernet.generate_key()


# Salva a chave em um arquivo chamado chave.key
# "wb" significa escrita em modo binário
with open("chave.key", "wb") as arquivo:
    arquivo.write(chave)


# Cria um objeto Fernet utilizando a chave gerada
fernet = Fernet(chave)


# Abre o arquivo original em modo de leitura binária
with open("mensagem.txt", "rb") as arquivo:

    # Lê todo o conteúdo do arquivo
    conteudo = arquivo.read()


# Criptografa o conteúdo utilizando a chave Fernet
criptografado = fernet.encrypt(conteudo)


# Cria um novo arquivo para armazenar o conteúdo criptografado
with open("mensagem_criptografada.txt", "wb") as arquivo:

    # Escreve os dados criptografados no novo arquivo
    arquivo.write(criptografado)


# Informa que a criptografia foi concluída
print("Arquivo criptografado!")
