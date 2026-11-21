from PIL import Image
from PIL.ExifTags import TAGS
import os


def investigar(caminho):
    if not os.path.isfile(caminho):
        print("Imagem não encontrada.")
        return

    try:
        imagem = Image.open(caminho)

        print("\nINFORMAÇÕES DA IMAGEM")
        print("Formato:", imagem.format)
        print("Dimensões:", imagem.size)
        print("Modo:", imagem.mode)
        print("Tamanho:", os.path.getsize(caminho), "bytes")

        exif = imagem.getexif()

        print("\nMETADADOS EXIF")

        if not exif:
            print("Nenhum metadado EXIF encontrado.")

        for codigo, valor in exif.items():
            nome = TAGS.get(codigo, codigo)
            print(f"{nome}: {valor}")

    except Exception as erro:
        print("Erro ao analisar imagem:", erro)


if __name__ == "__main__":
    caminho = input("Caminho da imagem: ")
    investigar(caminho)