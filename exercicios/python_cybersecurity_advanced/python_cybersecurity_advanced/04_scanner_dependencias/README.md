# Scanner de dependências Python

Interface simples para executar `pip-audit` contra um arquivo de requisitos, resumir vulnerabilidades conhecidas e salvar um relatório JSON.

## Estrutura
```text
04_scanner_dependencias/
├── main.py
├── requirements.txt
├── requirements-audit.txt
└── README.md
```

## Instalação
Use um ambiente virtual e instale a ferramenta:
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Execução
```bash
python main.py -r requirements-audit.txt -o audit-report.json
```

O scanner consulta a base de vulnerabilidades usada pelo pip-audit; portanto, requer conexão com a internet para obter dados atualizados. O arquivo `requirements-audit.txt` contém versões antigas apenas para demonstrar o fluxo; não instale essas dependências em ambiente de produção.

## Interpretação
O relatório lista pacotes, versões, identificadores de vulnerabilidade e versões corrigidas quando disponíveis. Um resultado sem vulnerabilidades conhecidas não prova que o software está seguro.

## Boas práticas
- Revise cada atualização antes de aplicá-la.
- Teste atualizações em ambiente isolado.
- Fixe versões e mantenha inventário de dependências.
- Não execute auditoria com credenciais ou tokens embutidos em arquivos compartilhados.
