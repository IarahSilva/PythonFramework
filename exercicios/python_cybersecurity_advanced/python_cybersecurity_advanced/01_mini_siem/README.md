# Mini SIEM em Python

Mini SIEM local para importar eventos JSON Lines, armazená-los em SQLite, executar regras simples de correlação e consultar alertas.

## Recursos
- Ingestão de eventos JSONL com validação básica de timestamp.
- Banco SQLite criado automaticamente (`siem.db`).
- Regras de exemplo para falhas de login, acesso administrativo e detecção de malware.
- Relatório dos últimos alertas.

## Estrutura
```text
01_mini_siem/
├── main.py
├── sample_events.jsonl
├── requirements.txt
└── README.md
```

## Execução
Requer Python 3.10 ou superior. Não há dependências externas.

```bash
python main.py ingest sample_events.jsonl
python main.py detect
python main.py report
```

A regra de falhas de login dispara com 5 eventos `login_failed` do mesmo IP dentro de 10 minutos, considerando como referência o evento mais recente daquele tipo importado. Isso permite reproduzir o teste com os timestamps fixos do arquivo de exemplo.

## Formato de evento
Cada linha deve ser um objeto JSON:
```json
{"timestamp":"2026-11-23T12:00:00+00:00","source":"auth","event_type":"login_failed","username":"admin","src_ip":"192.0.2.10","details":{}}
```

## Limitações e segurança
Projeto educacional, não substitui um SIEM de produção. As regras são demonstrativas, não há gerenciamento de identidade, retenção, alta disponibilidade ou proteção do banco. Use logs de laboratório e proteja dados pessoais. Em produção, valide esquema, sincronize relógios, controle acesso e evite registrar segredos.
