
# Cria um laço infinito para manter o programa em execução
while True:

    try:
        # Solicita ao usuário que digite um número inteiro
        num = int(input("Insira um número inteiro: "))

        # Exibe o número digitado
        print(num)

        # Pergunta se o usuário deseja encerrar o programa
        op = input("Deseja sair (sair)? ")

        # Verifica se a resposta foi "sair"
        if op == "sair":

            # Exibe a mensagem de encerramento
            print("ENCERRANDO.....")

            # Interrompe o laço e encerra o programa
            break

    except:
        # Executa caso ocorra algum erro dentro do try
        print("Código em execução....")
