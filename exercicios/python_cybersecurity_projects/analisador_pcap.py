from scapy.all import rdpcap, IP, TCP, UDP, ICMP
from collections import Counter
import sys


def analisar(caminho):
    pacotes = rdpcap(caminho)

    protocolos = Counter()
    ips = Counter()
    portas = Counter()

    for pacote in pacotes:

        if IP in pacote:
            ip = pacote[IP]

            ips[ip.src] += 1
            ips[ip.dst] += 1

            if TCP in pacote:
                protocolos["TCP"] += 1
                portas[pacote[TCP].dport] += 1

            elif UDP in pacote:
                protocolos["UDP"] += 1
                portas[pacote[UDP].dport] += 1

            elif ICMP in pacote:
                protocolos["ICMP"] += 1

            else:
                protocolos["OUTROS"] += 1

    print("Total de pacotes:", len(pacotes))

    print("\nProtocolos:")
    for protocolo, total in protocolos.items():
        print(protocolo, total)

    print("\nIPs mais frequentes:")
    for ip, total in ips.most_common(10):
        print(ip, total)

    print("\nPortas de destino:")
    for porta, total in portas.most_common(10):
        print(porta, total)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python analisador_pcap.py arquivo.pcap")
    else:
        analisar(sys.argv[1])