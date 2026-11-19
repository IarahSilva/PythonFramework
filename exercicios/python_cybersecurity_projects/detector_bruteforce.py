from collections import defaultdict
from datetime import datetime, timedelta

LOGS = [
    ("192.168.1.10", "2026-11-17 10:00:00", "FAIL"),
    ("192.168.1.10", "2026-11-17 10:00:10", "FAIL"),
    ("192.168.1.10", "2026-11-17 10:00:20", "FAIL"),
    ("192.168.1.10", "2026-11-17 10:00:30", "FAIL"),
    ("192.168.1.20", "2026-11-17 10:01:00", "SUCCESS"),
]


def detectar_bruteforce(logs, limite=3):
    tentativas = defaultdict(list)

    for ip, horario, status in logs:
        if status != "FAIL":
            continue

        momento = datetime.strptime(
            horario, "%Y-%m-%d %H:%M:%S"
        )

        tentativas[ip].append(momento)

    for ip, horarios in tentativas.items():
        horarios.sort()

        for i, inicio in enumerate(horarios):
            fim = inicio + timedelta(minutes=1)

            quantidade = sum(
                inicio <= h <= fim for h in horarios
            )

            if quantidade >= limite:
                print(f"ALERTA: possível força bruta!")
                print(f"IP: {ip}")
                print(f"Tentativas: {quantidade}")
                break


detectar_bruteforce(LOGS)

//Terminal:
//ALERTA: possível força bruta!
//IP: 192.168.1.10
//Tentativas: 4