import hashlib
import os

ASSINATURAS = {
    b"\x4D\x5A": "Executável Windows (PE)",
    b"\x7FELF": "Executável ELF",
    b"\x50\x4B\x03\x04": "Arquivo ZIP",
    b"%PDF": "Documento PDF",
    b"\x89PNG\r\n\x1a\n": "Imagem PNG",
    b"\xFF\xD8\xFF": "Imagem JPEG"
}


def analisar(caminho):
    if not os.path.isfile(caminho):
        print("Arquivo não encontrado.")
        return

    with open(caminho, "rb") as arquivo:
        inicio = arquivo.read(16)

    sha256 = hashlib.sha256()

    with open(caminho, "rb") as arquivo:
        for bloco in iter(
            lambda: arquivo.read(4096), b""
        ):
            sha256.update(bloco)

    tipo = "Formato desconhecido"

    for assinatura, descricao in ASSINATURAS.items():
        if inicio.startswith(assinatura):
            tipo = descricao
            break

    extensao = os.path.splitext(caminho)[1]

    print("\nRELATÓRIO DO ARQUIVO")
    print("Nome:", os.path.basename(caminho))
    print("Tamanho:", os.path.getsize(caminho), "bytes")
    print("Extensão:", extensao)
    print("Formato detectado:", tipo)
    print("SHA-256:", sha256.hexdigest())

    if extensao.lower() in [".exe", ".dll", ".bat", ".ps1"]:
        print("ATENÇÃO: arquivo executável ou script.")


if __name__ == "__main__":
    caminho = input("Caminho do arquivo: ")
    analisar(caminho)

//Terminal:
//RELATÓRIO DO ARQUIVO

//Nome: programa.exe
//Tamanho: 20480 bytes
//Extensão: .exe
//Formato detectado: Executável Windows (PE)
//SHA-256: 7f83b165...
//ATENÇÃO: arquivo executável ou script.