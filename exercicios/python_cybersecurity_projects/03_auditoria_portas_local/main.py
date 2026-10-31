import argparse, socket

def aberta(host, porta):
    try:
        with socket.create_connection((host, porta), timeout=0.4): return True
    except OSError: return False

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Use apenas em hosts próprios ou autorizados.")
    p.add_argument("host")
    p.add_argument("--inicio", type=int, default=1)
    p.add_argument("--fim", type=int, default=1024)
    a = p.parse_args()
    if not 1 <= a.inicio <= a.fim <= 65535: p.error("Intervalo inválido.")
    for porta in range(a.inicio, a.fim + 1):
        if aberta(a.host, porta): print(f"TCP {porta}: ABERTA")
