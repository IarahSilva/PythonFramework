import unicodedata
import os


def analisar(caminho):
    if not os.path.isfile(caminho):
        print("Arquivo não encontrado.")
        return

    with open(caminho, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    suspeitos = []

    for posicao, caractere in enumerate(texto):
        categoria = unicodedata.category(caractere)

        if categoria in ("Cf", "Cc", "Cs"):
            suspeitos.append(
                (posicao, ord(caractere), categoria)
            )

    print("\nANÁLISE DE CARACTERES")
    print("Total de caracteres:", len(texto))
    print("Caracteres suspeitos:", len(suspeitos))

    for posicao, codigo, categoria in suspeitos:
        nome = unicodedata.name(
            chr(codigo), "SEM NOME"
        )

        print(
            f"Posição: {posicao} | "
            f"Unicode: U+{codigo:04X} | "
            f"Categoria: {categoria} | "
            f"Nome: {nome}"
        )


if __name__ == "__main__":
    caminho = input("Arquivo de texto: ")
    analisar(caminho)

#Terminal:

#ANÁLISE DE CARACTERES

#Total de caracteres: 35
#Caracteres suspeitos: 1

#Posição: 12
#Unicode: U+200B
#Categoria: Cf
#Nome: ZERO WIDTH SPACE