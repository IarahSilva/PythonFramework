import re
from collections import Counter

log = """
192.168.0.1 acessou o servidor
10.0.0.2 acessou o servidor
192.168.0.1 tentou login
172.16.0.5 acessou o servidor
192.168.0.1 tentou login
"""

ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", log)

frequencia = Counter(ips)

for ip, quantidade in frequencia.items():
    print(f"IP: {ip} | Ocorrências: {quantidade}")