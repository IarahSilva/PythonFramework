senha = input("Digite sua senha: ")

if len(senha) < 6:
    print("Senha fraca")
elif len(senha) < 10:
    print("Senha média")
else:
    print("Senha forte")


#================================
#    VERIFICADOR DE SENHAS
#================================

#Digite sua senha: MinhaSenha123!

#Analisando senha...

#Tamanho: Adequado
#Números: Sim
#Letras: Sim
#Caracteres especiais: Sim

#Resultado: SENHA FORTE!