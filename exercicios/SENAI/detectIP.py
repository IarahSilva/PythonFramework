
# Importa a biblioteca de expressões regulares
import re

# Importa Counter para contar quantas vezes cada IP aparece
from collections import Counter


# Texto simulando um arquivo de log de acessos
log = """
192.168.0.1 acessou o servidor
10.0.0.2 acessou o servidor
192.168.0.1 tentou login
172.16.0.5 acessou o servidor
192.168.0.1 tentou login
"""


# Procura todos os endereços IP dentro do texto
# \d{1,3} = procura de 1 a 3 números
# \. = procura um ponto
# {3} = repete esse padrão três vezes
# \b = define os limites do endereço
ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", log)


# Conta quantas vezes cada endereço IP aparece
frequencia = Counter(ips)


# Percorre os IPs e suas respectivas quantidades
for ip, quantidade in frequencia.items():

    # Exibe o endereço IP e o número de ocorrências
    print(f"IP: {ip} | Ocorrências: {quantidade}")
