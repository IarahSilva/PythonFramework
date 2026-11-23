from collections import defaultdict

registros = [
    ("192.168.1.10", "falha"),
    ("192.168.1.10", "falha"),
    ("192.168.1.10", "falha"),
    ("10.0.0.5", "sucesso"),
    ("172.16.0.2", "falha")
]

tentativas = defaultdict(int)

for ip, status in registros:
    if status == "falha":
        tentativas[ip] += 1

for ip, quantidade in tentativas.items():
    if quantidade >= 3:
        print(f"ALERTA: {ip} teve {quantidade} falhas!")