from cryptography.fernet import Fernet

chave = Fernet.generate_key()

with open("chave.key", "wb") as arquivo:
    arquivo.write(chave)

fernet = Fernet(chave)

with open("mensagem.txt", "rb") as arquivo:
    conteudo = arquivo.read()

criptografado = fernet.encrypt(conteudo)

with open("mensagem_criptografada.txt", "wb") as arquivo:
    arquivo.write(criptografado)

print("Arquivo criptografado!")