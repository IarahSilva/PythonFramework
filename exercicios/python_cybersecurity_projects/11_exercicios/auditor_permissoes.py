import os
import stat


def auditar(pasta):
    for raiz, diretorios, arquivos in os.walk(pasta):

        for nome in diretorios + arquivos:
            caminho = os.path.join(raiz, nome)

            try:
                modo = stat.S_IMODE(
                    os.stat(caminho).st_mode
                )

                permissao = oct(modo)

                # Verifica se todos podem escrever
                if modo & stat.S_IWOTH:
                    print("[RISCO] Escrita liberada para todos:")
                    print(caminho, permissao)

                # Verifica se todos podem executar
                if modo & stat.S_IXOTH:
                    print("[ATENÇÃO] Execução liberada para todos:")
                    print(caminho, permissao)

            except OSError as erro:
                print("Erro:", caminho, erro)


if __name__ == "__main__":
    pasta = input("Diretório para auditar: ")

    if os.path.isdir(pasta):
        auditar(pasta)
    else:
        print("Diretório inválido.")


//Diretório para auditar: ./laboratorio

//[RISCO] Escrita liberada para todos:
//./laboratorio/config.txt 0o666