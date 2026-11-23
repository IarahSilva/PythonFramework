num = int(input("Insira um número inteiro: "))
fatorial = 1

for i in range(num, 0, -1):
    fatorial = fatorial * num

print(fatorial)