# Detector heurístico de phishing

Analisa arquivos `.eml` ou `.txt`, extrai URLs e procura sinais suspeitos, como urgência, encurtadores, URL sem HTTPS e hosts que parecem endereços IP.

## Estrutura
```text
02_detector_phishing/
├── main.py
├── sample_email.eml
├── requirements.txt
└── README.md
```

## Execução
Python 3.10+; sem dependências externas.

```bash
python main.py sample_email.eml
```

Também aceita texto:
```bash
python main.py mensagem.txt
```

## Exemplo de saída
O e-mail de demonstração deve apontar linguagem de urgência e URL com HTTP/encurtador.

## Limitações
A pontuação é heurística, não é um classificador treinado e não confirma phishing. HTTPS não garante legitimidade; remetentes podem ser falsificados; links podem redirecionar. O projeto não visita URLs nem baixa anexos. Analise somente mensagens que você tem autorização para examinar e não use e-mails reais com dados sensíveis em repositórios públicos.
