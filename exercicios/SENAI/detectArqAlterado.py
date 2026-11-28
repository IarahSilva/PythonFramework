
import hashlib

# Função responsável por calcular o hash do arquivo
def calcular_hash(caminho):

    # Cria um objeto para calcular o hash usando SHA-256
    sha256 = hashlib.sha256()

    # Abre o arquivo em modo de leitura binária ("rb")
    with open(caminho, "rb") as arquivo:

        # Lê o arquivo em blocos de 4096 bytes
        # Continua lendo até chegar ao final do arquivo (b"")
        for bloco in iter(lambda: arquivo.read(4096), b""):

            # Atualiza o hash com os dados de cada bloco
            sha256.update(bloco)

    # Retorna o hash calculado em formato hexadecimal
    return sha256.hexdigest()


# Nome do arquivo que será monitorado
arquivo = "documento.txt"

# Calcula e armazena o hash original do arquivo
hash_original = calcular_hash(arquivo)

# Aguarda o usuário alterar o arquivo
input("Altere o arquivo e pressione ENTER...")

# Calcula novamente o hash após a alteração
hash_atual = calcular_hash(arquivo)

# Compara o hash original com o hash atual
if hash_original != hash_atual:

    # Se forem diferentes, significa que o conteúdo foi alterado
    print("ALERTA: Arquivo modificado!")

else:

    # Se forem iguais, nenhuma alteração foi detectada
    print("Nenhuma alteração detectada.")
