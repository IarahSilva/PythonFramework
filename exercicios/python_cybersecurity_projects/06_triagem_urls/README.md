# 06 Triagem Urls

Aponta sinais simples de risco em URLs sem visitar o endereço.

## Requisitos
- Python 3.10 ou superior
- Dependências no `requirements.txt`

## Instalação
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

## Execução
```bash
python main.py https://exemplo.com/login
```
\nA análise é heurística, não visita a URL e não garante segurança.\n
## Estrutura
- `main.py`: código-fonte
- `requirements.txt`: dependências
- `README.md`: documentação e instruções

## Uso responsável
Projeto educacional de segurança defensiva. Use apenas em sistemas, arquivos e redes próprios ou autorizados.
