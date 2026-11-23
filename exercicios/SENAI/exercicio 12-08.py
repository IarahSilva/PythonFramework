while True:
    try:
      num = int(input("Insira um número inteiro: "))
      print(num)
      op = input("Deseja sair (sair)? ")

      if op == "sair":
        print("ENCERRANDO.....")
        break
    except:
       print("Código em execução....")
