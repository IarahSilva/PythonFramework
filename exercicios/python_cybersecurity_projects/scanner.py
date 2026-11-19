import socket

def verificar_porta(host, porta):
    cliente = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    cliente.settimeout(0.5)

    try:
        resultado = cliente.connect_ex((host, porta))

        if resultado == 0:
            print(f"Porta {porta}: ABERTA")

    except socket.error as erro:
        print("Erro:", erro)

    finally:
        cliente.close()


host = "127.0.0.1"

portas = [
    21, 22, 23, 25, 53,
    80, 110, 143, 443, 3306,
    5432, 8080
]

print("Analisando:", host)

for porta in portas:
    verificar_porta(host, porta)

print("Análise finalizada.")