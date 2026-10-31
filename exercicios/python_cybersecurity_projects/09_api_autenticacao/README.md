# 09 Api Autenticacao

API didática com FastAPI e hash de senha bcrypt.

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
uvicorn main:app --reload  # docs em /docs
```
\nAPI didática: usuários ficam em memória e somem ao reiniciar. Não use em produção nem com senhas reais.\n
## Estrutura
- `main.py`: código-fonte
- `requirements.txt`: dependências
- `README.md`: documentação e instruções

## Uso responsável
Projeto educacional de segurança defensiva. Use apenas em sistemas, arquivos e redes próprios ou autorizados.
