# ---------------------------------------------------------
# FUNÇÕES DE CÁLCULO (Lógica do sistema)
# ---------------------------------------------------------

def calcular_valor_porcentagem(valor_base: float, porcentagem: float) -> float:
    """
    Calcula o valor nominal de uma porcentagem sobre um montante.
    Exemplo: 10% de R$ 200,00 -> retorna 20.0
    """
    # Dividimos a porcentagem por 100 para obter o valor decimal (ex: 15% vira 0.15)
    resultado = valor_base * (porcentagem / 100)
    return resultado

# ---------------------------------------------------------
# FUNÇÃO DE INTERFACE (Aparência no terminal)
# ---------------------------------------------------------

def exibir_relatorio(bruto, p_desc, v_desc, p_taxa, v_taxa, final):
    """
    Organiza as informações de forma visual para o aluno.
    Exibe tanto a porcentagem escolhida quanto o valor em reais calculado.
    """
    print("\n" + "="*35)
    print(f"{'RECIBO PERSONALIZADO':^35}")
    print("="*35)
    print(f"Valor Original:     R$ {bruto:>8.2f}")
    print(f"(-) Desconto ({p_desc:>2.0f}%): R$ {v_desc:>8.2f}")
    print(f"(+) Taxa ({p_taxa:>2.0f}%):     R$ {v_taxa:>8.2f}")
    print("-" * 35)
    print(f"TOTAL FINAL:        R$ {final:>8.2f}")
    print("="*35 + "\n")

# ---------------------------------------------------------
# FUNÇÃO PRINCIPAL (Fluxo de execução)
# ---------------------------------------------------------

def executar_sistema():
    """
    Coordena a entrada de dados flexível e processa os resultados.
    """
    # 1. Coleta de dados (Entradas do usuário)
    print("--- Configuração de Venda ---")
    valor_venda = float(input("Digite o valor do produto: "))
    perc_desconto = float(input("Digite a porcentagem de desconto (ex: 10): "))
    perc_taxa = float(input("Digite a porcentagem da taxa (ex: 5): "))

    # 2. Validação simples: o valor da venda deve ser positivo
    if valor_venda > 0:
        
        # 3. Processamento: Chamamos a mesma função de cálculo para objetivos diferentes
        # Calculamos o valor em Reais do desconto
        valor_do_desconto = calcular_valor_porcentagem(valor_venda, perc_desconto)
        
        # Calculamos o valor em Reais da taxa
        valor_da_taxa = calcular_valor_porcentagem(valor_venda, perc_taxa)
        
        # 4. Cálculo do valor final (Bruto - Desconto + Taxa)
        valor_final = valor_venda - valor_do_desconto + valor_da_taxa
        
        # 5. Saída: Exibimos o relatório com todos os dados
        exibir_relatorio(valor_venda, perc_desconto, valor_do_desconto, 
                         perc_taxa, valor_da_taxa, valor_final)
    else:
        print("\nErro: O valor da venda precisa ser maior que zero.")

# ---------------------------------------------------------
# INICIALIZAÇÃO
# ---------------------------------------------------------

# Inicia o programa
executar_sistema()