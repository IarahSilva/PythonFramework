
# Cria um laço infinito para repetir até a operação ser concluída corretamente
while True:

    try:
        # Cria uma lista com valores inteiros
        lista = [2, 4, 10, 45, 22]

        # Solicita ao usuário um índice da lista
        ind = int(input("Insira o índice que selecionou: "))

        # Solicita um número que será utilizado como divisor
        divisor = int(input("Insira um divisor: "))

        # Acessa o elemento da lista conforme o índice informado
        indice = lista[ind]

        # Exibe o elemento selecionado
        print(f"Opção {indice} selecionada...")

        # Verifica se o divisor é diferente de zero
        if divisor != 0:

            # Realiza a divisão do elemento pelo divisor
            divisao = (indice / divisor)

            # Exibe o resultado da divisão
            print(f"O resultado é: {divisao}")

            # Encerra o laço após a operação ser concluída
            break

    except IndexError:
        # Executa quando o índice informado não existe na lista
        print("Opção não localizada...Tente Novamente.")

    except ValueError:
        # Executa quando o usuário digita algo que não pode ser convertido em inteiro
        print("Erro de Valor: Por favor, digite apenas números inteiros.")

    except ZeroDivisionError:
        # Executa quando ocorre uma tentativa de divisão por zero
        print("Erro de Divisão: O segundo número não pode ser zero.")
