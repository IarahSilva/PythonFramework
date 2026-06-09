def aplicar_desconto(preco, perc):
    desconto = (perc / 100) * 100
    return preco - desconto

preco = float(input("Insira o valor do preço: "))
perc = float(input("Informe qual foi o percentual de desconto em porcentagem(%): "))
preco_final = aplicar_desconto(preco, perc)
print(f"O preço final com o desconto incluso foi de: R$ {preco_final}")