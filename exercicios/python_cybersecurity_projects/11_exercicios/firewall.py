from collections import Counter
import re

logs = [
    "192.168.1.10 BLOCKED",
    "192.168.1.20 ALLOWED",
    "192.168.1.10 BLOCKED",
    "10.0.0.5 BLOCKED",
    "192.168.1.10 BLOCKED",
    "10.0.0.5 ALLOWED"
]


def analisar_logs(registros):
    bloqueios = Counter()
    permitidos = 0

    for linha in registros:
        partes = linha.split()

        if len(partes) != 2:
            continue

        ip, status = partes

        if not re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", ip):
            continue

        if status == "BLOCKED":
            bloqueios[ip] += 1

        elif status == "ALLOWED":
            permitidos += 1

    print("Conexões permitidas:", permitidos)
    print("\nIPs bloqueados:")

    for ip, quantidade in bloqueios.items():
        print(f"{ip}: {quantidade} bloqueios")

        if quantidade >= 3:
            print("ALERTA: muitas tentativas bloqueadas!")


analisar_logs(logs)

#Terminal:
#Conexões permitidas: 2

#IPs bloqueados:
#192.168.1.10: 3 bloqueios
#ALERTA: muitas tentativas bloqueadas!
#10.0.0.5: 1 bloqueios