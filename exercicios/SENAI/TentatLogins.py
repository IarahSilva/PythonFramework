# Importa defaultdict para criar um dicionário com valor inicial automático
from collections import defaultdict


# Lista de registros contendo endereço IP e status de acesso
registros = [
    ("192.168.1.10", "falha"),
    ("192.168.1.10", "falha"),
    ("192.168.1.10", "falha"),
    ("10.0.0.5", "sucesso"),
    ("172.16.0.2", "falha")
]


# Cria um dicionário para armazenar a quantidade de falhas por IP
# Cada IP começa com o contador igual a zero
tentativas = defaultdict(int)


# Percorre todos os registros da lista
for ip, status in registros:

    # Verifica se o acesso realizado foi uma falha
    if status == "falha":

        # Incrementa em 1 a quantidade de falhas daquele endereço IP
        tentativas[ip] += 1


# Percorre o dicionário com os IPs e suas respectivas quantidades de falhas
for ip, quantidade in tentativas.items():

    # Verifica se o IP apresentou três ou mais falhas
    if quantidade >= 3:

        # Exibe um alerta de segurança
        print(f"ALERTA: {ip} teve {quantidade} falhas!")