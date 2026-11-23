# ---------------------------------------------------------
# FUNÇÃO DE PROCESSAMENTO (Uso de Dicionário Nomeado)
# ---------------------------------------------------------

def exibir_dados_motor(modelo: str, **especificacoes):
    """
    O símbolo '**' (kwargs) permite que a função receba uma quantidade 
    variável de argumentos NOMEADOS (ex: potencia="5CV").
    O Python transforma esses argumentos em um dicionário (chave e valor).
    """
    print("\n" + "="*40)
    print(f"IDENTIFICAÇÃO DO MOTOR: {modelo}")
    print("="*40)
    print("ESPECIFICAÇÕES TÉCNICAS:")

    # O método .items() permite acessar a 'chave' (nome) e o 'valor' do dicionário
    for chave, valor in especificacoes.items():
        # Formatamos a chave para ficar em letras maiúsculas para o relatório
        print(f"  - {chave.upper()}: {valor}")
    
    print("-" * 40)
    print("Fim do Relatório Técnico\n")

# ---------------------------------------------------------
# FUNÇÃO PRINCIPAL (Interação com o usuário)
# ---------------------------------------------------------

def cadastrar_motor():
    """
    Coleta os dados do motor e demonstra a flexibilidade do **kwargs.
    """
    # 1. Entrada obrigatória (modelo)
    id_motor = input("Digite o modelo do motor (ex: WEG-X1): ")

    # 2. Simulação de coleta de dados variáveis
    # No VS Code, o aluno pode adicionar mais pares de chave=valor aqui
    # Os nomes (potencia, rpm, etc) viram as "chaves" do dicionário
    print(f"Processando especificações para o motor {id_motor}...")
    
    # Chamada da função passando argumentos nomeados
    exibir_dados_motor(
        id_motor, 
        potencia="7.5 CV", 
        rpm=1750, 
        tensao="380V", 
        frequencia="60Hz",
        protecao="IP55"
    )

# ---------------------------------------------------------
# INICIALIZAÇÃO
# ---------------------------------------------------------

# Executa o programa de cadastro
cadastrar_motor()