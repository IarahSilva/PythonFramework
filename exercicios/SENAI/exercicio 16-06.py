def verificacao(*, num: int) -> int:
    if(num % 2 == 0):
        return True
    else:
        return False
    
num = int(input("Insira um número inteiro: "))
resulVerificacao = verificacao(num=num)
print(f"O número digitado é: {resulVerificacao}")
