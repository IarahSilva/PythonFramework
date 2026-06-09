import saudacoes

print("Bem vindo usuario é dia ou noite? ")
op = input("Informe se é dia ou noite: ")
if op == "dia":
    saudacoes.bom_dia()
elif op == "noite":
    saudacoes.boa_noite()
else:
     print("Erro!")