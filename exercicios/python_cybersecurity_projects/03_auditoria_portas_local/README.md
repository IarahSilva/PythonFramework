# 03 Auditoria Portas Local

Testa portas TCP em um host autorizado.

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
python main.py 127.0.0.1 --inicio 1 --fim 1024
```
\n**Atenção:** use somente em hosts próprios ou com autorização explícita.\n
## Estrutura
- `main.py`: código-fonte
- `requirements.txt`: dependências
- `README.md`: documentação e instruções

## Uso responsável
Projeto educacional de segurança defensiva. Use apenas em sistemas, arquivos e redes próprios ou autorizados.
