# ---------------------------------------------------------
# FUNÇÕES DE PROCESSAMENTO (Lógica de Agrupamento)
# ---------------------------------------------------------

def somar_leituras_sensores(*leituras: float) -> float:
    """
    O símbolo '*' (args) permite que a função receba uma quantidade 
    variável de argumentos. O Python transforma tudo em uma tupla.
    """
    # 'sum' é uma função nativa que soma todos os itens de uma lista/tupla
    total = sum(leituras)
    return total

def exibir_relatorio_sensores(lista_valores, total_soma):
    """
    Formata a saída para mostrar quantos sensores foram lidos
    e qual o resultado final da operação.
    """
    # len() conta quantos itens existem dentro da coleção de dados
    quantidade = len(lista_valores)
    
    print("\n" + "="*40)
    print(f"{'SISTEMA DE MONITORAMENTO MULTI-SENSOR':^40}")
    print("="*40)
    print(f"Número de sensores ativos: {quantidade}")
    print(f"Valores individuais:      {lista_valores}")
    print("-" * 40)
    print(f"SOMA TOTAL DAS LEITURAS:  {total_soma:.2f}")
    print("="*40 + "\n")

# ---------------------------------------------------------
# FUNÇÃO PRINCIPAL (Fluxo de execução)
# ---------------------------------------------------------

def executar_sistema():
    """
    Simula a coleta de dados e organiza a chamada das funções.
    """
    # No VS Code, você pode alterar estes valores livremente para testar
    # Adicione ou remova números separados por vírgula
    print("Iniciando coleta de dados dos sensores...")
    
    # 1. Armazenamos os valores em uma variável para poder mostrar depois
    dados_sensores = (10.5, 20.0, 5.2, 12.8, 7.4)
    
    # 2. Chamamos a função de soma usando o '*' para "desempacotar" a tupla
    # Isso envia cada número como um argumento separado para a função
    resultado = somar_leituras_sensores(*dados_sensores)

    # 3. Exibição didática
    exibir_relatorio_sensores(dados_sensores, resultado)

# ---------------------------------------------------------
# INICIALIZAÇÃO
# ---------------------------------------------------------

# Roda o script
executar_sistema()