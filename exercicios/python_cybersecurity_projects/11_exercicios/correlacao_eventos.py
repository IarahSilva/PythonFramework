from datetime import datetime, timedelta
from collections import defaultdict

EVENTOS = [
    ("192.168.1.10", "2026-11-17 10:00:00", "FAIL"),
    ("192.168.1.10", "2026-11-17 10:00:10", "FAIL"),
    ("192.168.1.10", "2026-11-17 10:00:20", "FAIL"),
    ("192.168.1.10", "2026-11-17 10:00:30", "SUCCESS"),

    ("192.168.1.20", "2026-11-17 10:01:00", "SUCCESS"),
    ("192.168.1.30", "2026-11-17 10:02:00", "FAIL")
]


def correlacionar(eventos):
    dados = defaultdict(list)

    for ip, horario, tipo in eventos:
        momento = datetime.strptime(
            horario, "%Y-%m-%d %H:%M:%S"
        )

        dados[ip].append((momento, tipo))

    print("\nANÁLISE DE CORRELAÇÃO")

    for ip, registros in dados.items():
        registros.sort()

        for i, (momento, tipo) in enumerate(registros):

            if tipo != "SUCCESS":
                continue

            inicio = momento - timedelta(minutes=5)

            falhas = sum(
                1
                for horario, evento in registros[:i]
                if inicio <= horario < momento
                and evento == "FAIL"
            )

            if falhas >= 3:
                print("\n[ALERTA DE SEGURANÇA]")
                print("IP:", ip)
                print("Falhas anteriores:", falhas)
                print("Evento posterior: Login bem-sucedido")
                print("Possível comprometimento de conta.")


if __name__ == "__main__":
    correlacionar(EVENTOS)