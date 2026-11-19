import os
import hashlib
import time


PASTA = "arquivos_monitorados"


def hash_arquivo(caminho):
    sha = hashlib.sha256()

    with open(caminho, "rb") as arquivo:
        for bloco in iter(
            lambda: arquivo.read(4096), b""
        ):
            sha.update(bloco)

    return sha.hexdigest()


def criar_snapshot():
    snapshot = {}

    for raiz, diretorios, arquivos in os.walk(PASTA):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)

            try:
                snapshot[caminho] = hash_arquivo(caminho)
            except OSError:
                pass

    return snapshot


def comparar(antigo, novo):
    for arquivo in novo:
        if arquivo not in antigo:
            print("[NOVO]", arquivo)

        elif antigo[arquivo] != novo[arquivo]:
            print("[MODIFICADO]", arquivo)

    for arquivo in antigo:
        if arquivo not in novo:
            print("[REMOVIDO]", arquivo)


if __name__ == "__main__":
    os.makedirs(PASTA, exist_ok=True)

    print("Criando snapshot inicial...")
    anterior = criar_snapshot()

    print("Monitoramento iniciado. CTRL+C para parar.")

    try:
        while True:
            time.sleep(5)

            atual = criar_snapshot()
            comparar(anterior, atual)

            anterior = atual

    except KeyboardInterrupt:
        print("\nMonitoramento encerrado.")

//Terminal:
//Criando snapshot inicial...
//Monitoramento iniciado. CTRL+C para parar.

//[MODIFICADO] arquivos_monitorados//
/config.txt
//[NOVO] arquivos_monitorados//relatorio.pdf
//[REMOVIDO] arquivos_monitorados/teste.txt