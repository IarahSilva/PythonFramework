def e_par(numero):
    if numero % 2 == 0:
        return print(f"O número {numero} é Par!")
    else: 
        return print(f"O número {numero} é Impar")
    
numero = int(input("Insira um número: "))
e_par(numero)
