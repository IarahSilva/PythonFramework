import ipaddress
import json

IOC = {
    "203.0.113.10",
    "198.51.100.20",
    "192.0.2.50"
}

logs = [
    "Conexão recebida de 192.168.1.10",
    "Conexão recebida de 203.0.113.10",
    "Conexão recebida de 198.51.100.20",
    "Conexão recebida de 10.0.0.5"
]


def extrair_ips(texto):
    encontrados = []

    for palavra in texto.split():
        ip = palavra.strip(".,:;()[]")

        try:
            ipaddress.ip_address(ip)
            encontrados.append(ip)
        except ValueError:
            pass

    return encontrados


def analisar(registros):
    alertas = []

    for linha in registros:
        for ip in extrair_ips(linha):
            if ip in IOC:
                alertas.append({
                    "ip": ip,
                    "registro": linha
                })

    print("RELATÓRIO DE INDICADORES")

    for alerta in alertas:
        print("IP suspeito:", alerta["ip"])
        print("Registro:", alerta["registro"])
        print("---")

    print("Total de alertas:", len(alertas))


analisar(logs)

#Terminal:
#RELATÓRIO DE INDICADORES

#IP suspeito: 203.0.113.10
#Registro: Conexão recebida de //203.0.113.10
#---
#IP suspeito: 198.51.100.20
#Registro: Conexão recebida de 198.51.100.20
#---
#Total de alertas: 2