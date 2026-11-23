import argparse
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

FEATURES = ["failed_logins", "bytes_sent", "connections", "hour"]

def train(input_csv, model_path):
    data = pd.read_csv(input_csv)
    missing = set(FEATURES) - set(data.columns)
    if missing:
        raise SystemExit(f"Colunas ausentes: {', '.join(sorted(missing))}")
    X = data[FEATURES].apply(pd.to_numeric, errors="coerce")
    if X.isna().any().any():
        raise SystemExit("Há valores vazios ou não numéricos nas colunas de análise.")
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("detector", IsolationForest(
            n_estimators=200,
            contamination=0.08,
            random_state=42
        ))
    ])
    model.fit(X)
    joblib.dump(model, model_path)
    print(f"Modelo treinado e salvo em {model_path}")
    print(f"Registros usados: {len(X)}")

def predict(input_csv, model_path):
    if not Path(model_path).is_file():
        raise SystemExit("Modelo não encontrado. Execute primeiro o comando train.")
    data = pd.read_csv(input_csv)
    missing = set(FEATURES) - set(data.columns)
    if missing:
        raise SystemExit(f"Colunas ausentes: {', '.join(sorted(missing))}")
    X = data[FEATURES].apply(pd.to_numeric, errors="coerce")
    if X.isna().any().any():
        raise SystemExit("Há valores vazios ou não numéricos nas colunas de análise.")
    model = joblib.load(model_path)
    data["resultado"] = model.predict(X)
    data["anomalia"] = data["resultado"].map({1: "NORMAL", -1: "ANOMALIA"})
    data["score_anomalia"] = model.decision_function(X)
    print(data[FEATURES + ["anomalia", "score_anomalia"]].to_string(index=False))
    output = "anomaly_results.csv"
    data.to_csv(output, index=False)
    print(f"\nResultado salvo em {output}")

def main():
    parser = argparse.ArgumentParser(description="Detector de anomalias em métricas de acesso.")
    sub = parser.add_subparsers(dest="command", required=True)
    p_train = sub.add_parser("train")
    p_train.add_argument("--input", default="sample_metrics.csv")
    p_train.add_argument("--model", default="anomaly_model.joblib")
    p_predict = sub.add_parser("predict")
    p_predict.add_argument("--input", default="sample_new_metrics.csv")
    p_predict.add_argument("--model", default="anomaly_model.joblib")
    args = parser.parse_args()
    if args.command == "train":
        train(args.input, args.model)
    else:
        predict(args.input, args.model)

if __name__ == "__main__":
    main()
