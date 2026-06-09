def converterCelsius(tempInicial: float):
    tempFahrenheit = ((tempInicial * 1.8) + 32)
    return tempFahrenheit

tempInicial = float(input("Insira a temperatura inicial: "))
tempCovertida = converterCelsius(tempInicial)
print(f"A temperatura atual é: {tempCovertida}")



