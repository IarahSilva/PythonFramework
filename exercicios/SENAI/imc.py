# Importa a biblioteca Tkinter para criar a interface gráfica
import tkinter as tk


# Função responsável por calcular o IMC
def calcular_imc():
    try:
        # Obtém o peso digitado e converte para número decimal
        peso = float(entry_peso.get())

        # Obtém a altura digitada e converte para número decimal
        altura = float(entry_altura.get())

        # Calcula o IMC: peso dividido pela altura ao quadrado
        imc = peso / (altura ** 2)

        # Verifica a classificação de acordo com o resultado do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"

        elif 18.5 <= imc < 25:
            classificacao = "Peso normal"

        elif 25 <= imc < 30:
            classificacao = "Sobrepeso"

        else:
            classificacao = "Obesidade"

        # Exibe o resultado e a classificação na interface
        label_resultado.config(
            text=f"Seu IMC é {imc:.2f}\nClassificação: {classificacao}"
        )

    # Trata erros caso o usuário digite letras ou valores inválidos
    except ValueError:
        label_resultado.config(
            text="Por favor, digite valores numéricos válidos."
        )


# --- Configuração da Janela ---

# Cria a janela principal da aplicação
janela = tk.Tk()

# Define o título da janela
janela.title("Calculadora de IMC")

# Define a largura e a altura da janela
janela.geometry("300x200")


# --- Widgets ---

# Cria o texto que identifica o campo de peso
tk.Label(janela, text="Peso (kg):").grid(
    row=0, column=0, padx=10, pady=5
)

# Cria o campo onde o usuário digita o peso
entry_peso = tk.Entry(janela)
entry_peso.grid(row=0, column=1, padx=10, pady=5)


# Cria o texto que identifica o campo de altura
tk.Label(janela, text="Altura (m):").grid(
    row=1, column=0, padx=10, pady=5
)

# Cria o campo onde o usuário digita a altura
entry_altura = tk.Entry(janela)
entry_altura.grid(row=1, column=1, padx=10, pady=5)


# Cria o botão que chama a função calcular_imc ao ser clicado
botao_calcular = tk.Button(
    janela,
    text="Calcular",
    command=calcular_imc
)

# Posiciona o botão na janela
botao_calcular.grid(
    row=2, column=0, columnspan=2, pady=10
)


# Cria o espaço onde será exibido o resultado do cálculo
label_resultado = tk.Label(
    janela,
    text="",
    font=("Arial", 10, "bold")
)

# Posiciona o resultado na janela
label_resultado.grid(
    row=3, column=0, columnspan=2, pady=5
)


# --- Inicia a Janela ---

# Mantém a janela aberta e aguardando interações do usuário
janela.mainloop()