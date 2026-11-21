import os
import time
from datetime import datetime

LOG = "sistema.log"

EVENTOS = {
    "FAILED LOGIN": "Tentativa de login malsucedida",
    "ACCESS DENIED": "Acesso negado",
    "UNAUTHORIZED": "Acesso não autorizado",
    "PRIVILEGE CHANGE": "Alteração de privilégio",
    "ACCOUNT LOCKED": "Conta bloqueada"
}


def analisar_linha(linha):
    texto = linha.upper()

    for evento, descricao in EVENTOS.items():
        if evento in texto:
            horario = datetime.now().strftime(
                "%H:%M:%S"
            )

            print(f"\n[{horario}] ALERTA")
            print("Evento:", descricao)
            print("Registro:", linha.strip())


def monitorar():
    if not os.path.exists(LOG):
        open(LOG, "a").close()

    print("Monitoramento iniciado...")

    with open(LOG, "r", encoding="utf-8") as arquivo:
        arquivo.seek(0, os.SEEK_END)

        while True:
            linha = arquivo.readline()

            if not linha:
                time.sleep(0.5)
                continue

            analisar_linha(linha)


if __name__ == "__main__":
    try:
        monitorar()
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado.")