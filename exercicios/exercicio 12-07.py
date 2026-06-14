while True:
 try:
    lista = [2, 4, 10, 45, 22]
    ind = int(input("Insira o índice que selecionou: "))
    divisor = int(input("Insira um divisor: "))
    
    indice = lista[ind]
    print(f"Opção {indice} selecionada...")
    if divisor != 0:
       divisao = (indice / divisor)
       print(f"O resultado é: {divisao}")
       break

 except IndexError:
   print("Opção não localizada...Tente Novamente.")

 except ValueError:
    print("Erro de Valor: Por favor, digite apenas números inteiros.")
 except ZeroDivisionError:
    print("Erro de Divisão: O segundo número não pode ser zero.")