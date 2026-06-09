# ---------------------------------------------------------
# FUNÇÃO DE VALIDAÇÃO (Lógica de Verificação)
# ---------------------------------------------------------

def esta_na_faixa(valor: float, limite_min: float, limite_max: float) -> bool:
    """
    Verifica se o valor está dentro de um intervalo personalizado.
    Retorna True (verdadeiro) se estiver entre os limites, ou False (falso) caso contrário.
    """
    # Verificação matemática: o valor deve ser maior ou igual ao mínimo
    # E também deve ser menor ou igual ao máximo
    status = limite_min <= valor <= limite_max
    return status

# ---------------------------------------------------------
# FUNÇÃO DE INTERFACE (Saída de dados)
# ---------------------------------------------------------

def exibir_resultado(valor: float, minimo: float, maximo: float, valido: bool):
    """
    Exibe uma mensagem didática baseada no resultado da validação.
    """
    print("\n" + "="*40)
    print(f"Relatório de Monitoramento")
    print("="*40)
    print(f"Valor lido:     {valor}")
    print(f"Faixa permitida: {minimo} até {maximo}")
    print("-" * 40)
    
    if valido:
        print("STATUS: [ OK ] - Leitura dentro dos limites.")
    else:
        print("STATUS: [ ERRO ] - Valor fora da faixa!")
    print("="*40 + "\n")

# ---------------------------------------------------------
# FUNÇÃO PRINCIPAL (Fluxo de execução)
# ---------------------------------------------------------

def executar_leitura_painel():
    """
    Permite que o usuário configure os limites e teste um valor.
    """
    # 1. Entrada de dados para configurar os limites (flexibilidade)
    print("--- Configuração do Sensor ---")
    min_config = float(input("Defina o limite MÍNIMO do sensor: "))
    max_config = float(input("Defina o limite MÁXIMO do sensor: "))
    
    # 2. Entrada do valor a ser testado
    valor_lido = float(input("\nDigite o valor atual lido no painel: "))

    # 3. Processamento: Chamada da função de validação
    # Passamos o valor lido e os limites que o usuário acabou de criar
    resultado_validacao = esta_na_faixa(valor_lido, min_config, max_config)

    # 4. Saída: Chamada da função que organiza o texto na tela
    exibir_resultado(valor_lido, min_config, max_config, resultado_validacao)

# ---------------------------------------------------------
# INICIALIZAÇÃO
# ---------------------------------------------------------

# Inicia o monitoramento
executar_leitura_painel()