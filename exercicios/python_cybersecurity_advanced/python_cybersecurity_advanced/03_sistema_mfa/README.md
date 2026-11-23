# Sistema MFA com TOTP

Demonstra autenticação em duas etapas: senha local + código temporário TOTP compatível com aplicativos autenticadores.

## Estrutura
```text
03_sistema_mfa/
├── main.py
├── requirements.txt
└── README.md
```

## Instalação
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

## Configuração
```bash
python main.py setup --user iara
```
Crie uma senha de pelo menos 12 caracteres. O programa imprime o segredo TOTP e tenta gerar `mfa_qr.png`, que pode ser importado em um autenticador compatível.

## Login
```bash
python main.py login
```
Digite a senha e o código de seis dígitos exibido no aplicativo autenticador.

## Arquivos gerados
- `mfa_user.json`: registro de demonstração com hash da senha e segredo TOTP.
- `password_salt.bin`: salt para derivação da senha.
- `mfa_qr.png`: QR Code de configuração, se a biblioteca estiver disponível.

## Segurança e limitações
Projeto educacional para execução local. O segredo TOTP e o hash ficam em arquivos locais; isso não é adequado para produção. Em um serviço real, armazene segredos cifrados, use banco protegido, controle tentativas, recuperação segura, sessões, CSRF e TLS. Não compartilhe o QR Code ou segredo. Para reiniciar o laboratório, faça backup e remova os arquivos locais gerados.
