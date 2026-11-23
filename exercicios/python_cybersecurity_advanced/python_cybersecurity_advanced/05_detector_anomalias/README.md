# Detector de anomalias com Isolation Forest

Treina um modelo não supervisionado para identificar registros de atividade que se afastam do padrão observado em métricas sintéticas de acesso.

## Estrutura
```text
05_detector_anomalias/
├── main.py
├── sample_metrics.csv
├── sample_new_metrics.csv
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

## Treinamento
```bash
python main.py train --input sample_metrics.csv
```

## Detecção
```bash
python main.py predict --input sample_new_metrics.csv
```

O programa cria `anomaly_model.joblib` e `anomaly_results.csv`.

## Dados esperados
O CSV precisa conter:
- `failed_logins`: falhas de autenticação observadas.
- `bytes_sent`: bytes enviados.
- `connections`: quantidade de conexões.
- `hour`: hora do dia (0–23).

## Interpretação e limitações
Isolation Forest identifica pontos estatisticamente incomuns; não determina intenção maliciosa. O modelo depende da representatividade dos dados de treinamento e do ajuste de `contamination`. Os CSVs fornecidos são sintéticos e servem apenas para demonstrar o fluxo. Em produção, valide dados, monitore drift, avalie falsos positivos e não tome ações automáticas com base apenas no modelo.
