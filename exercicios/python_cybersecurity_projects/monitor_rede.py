import psutil
from collections import Counter


def monitorar():
    conexoes = psutil.net_connections(kind="tcp")

    estados = Counter()

    print("\nCONEXÕES TCP")

    for conexao in conexoes:
        estados[conexao.status] += 1

        if conexao.raddr:
            destino = (
                f"{conexao.raddr.ip}:"
                f"{conexao.raddr.port}"
            )
        else:
            destino = "Sem destino remoto"

        if conexao.laddr:
            origem = (
                f"{conexao.laddr.ip}:"
                f"{conexao.laddr.port}"
            )
        else:
            origem = "Indisponível"

        print(
            f"PID: {conexao.pid} | "
            f"Origem: {origem} | "
            f"Destino: {destino} | "
            f"Estado: {conexao.status}"
        )

    print("\nRESUMO:")

    for estado, quantidade in estados.items():
        print(estado, quantidade)


if __name__ == "__main__":
    monitorar()

//pip install psutil