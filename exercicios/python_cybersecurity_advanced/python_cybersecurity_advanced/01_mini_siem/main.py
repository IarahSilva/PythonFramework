import argparse
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path("siem.db")

RULES = [
    {"name": "Muitas falhas de login", "event": "login_failed", "threshold": 5, "window_minutes": 10, "severity": "HIGH"},
    {"name": "Acesso administrativo", "event": "admin_login", "threshold": 1, "window_minutes": 60, "severity": "MEDIUM"},
    {"name": "Malware detectado", "event": "malware_detected", "threshold": 1, "window_minutes": 60, "severity": "CRITICAL"},
]

def connect():
    conn = sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY, timestamp TEXT NOT NULL, source TEXT,
        event_type TEXT NOT NULL, username TEXT, src_ip TEXT, details TEXT
    )""")
    conn.execute("""CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY, created_at TEXT NOT NULL, rule TEXT,
        severity TEXT, src_ip TEXT, count INTEGER, description TEXT
    )""")
    return conn

def ingest(path):
    conn = connect()
    count = 0
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
                timestamp = item.get("timestamp") or datetime.now(timezone.utc).isoformat()
                datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                event_type = str(item["event_type"])
                conn.execute(
                    "INSERT INTO events(timestamp,source,event_type,username,src_ip,details) VALUES(?,?,?,?,?,?)",
                    (timestamp, item.get("source", "unknown"), event_type,
                     item.get("username"), item.get("src_ip"), json.dumps(item.get("details", {}), ensure_ascii=False))
                )
                count += 1
            except (ValueError, KeyError, TypeError) as exc:
                print(f"[AVISO] Linha {line_no} ignorada: {exc}")
    conn.commit()
    conn.close()
    print(f"{count} evento(s) importado(s).")

def detect():
    conn = connect()
    conn.row_factory = sqlite3.Row
    created = 0
    for rule in RULES:
        rows = conn.execute(
            """SELECT src_ip, COUNT(*) AS total
               FROM events
               WHERE event_type = ?
                 AND datetime(timestamp) >= datetime(
                    (SELECT MAX(timestamp) FROM events WHERE event_type = ?), ?
                 )
               GROUP BY src_ip
               HAVING COUNT(*) >= ?""",
            (rule["event"], rule["event"], f'-{rule["window_minutes"]} minutes', rule["threshold"])
        ).fetchall()
        for row in rows:
            ip = row["src_ip"] or "desconhecido"
            description = f'{rule["name"]}: {row["total"]} evento(s) associados a {ip}.'
            conn.execute(
                "INSERT INTO alerts(created_at,rule,severity,src_ip,count,description) VALUES(?,?,?,?,?,?)",
                (datetime.now(timezone.utc).isoformat(), rule["name"], rule["severity"], ip, row["total"], description)
            )
            print(f'[{rule["severity"]}] {description}')
            created += 1
    conn.commit()
    conn.close()
    print(f"{created} alerta(s) criado(s).")

def report():
    conn = connect()
    print("\n=== RESUMO SIEM ===")
    print("Eventos:", conn.execute("SELECT COUNT(*) FROM events").fetchone()[0])
    print("Alertas:", conn.execute("SELECT COUNT(*) FROM alerts").fetchone()[0])
    rows = conn.execute("SELECT created_at,severity,description FROM alerts ORDER BY id DESC LIMIT 20")
    for created_at, severity, description in rows:
        print(f"{created_at} [{severity}] {description}")
    conn.close()

def main():
    parser = argparse.ArgumentParser(description="Mini SIEM local para eventos de laboratório.")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("ingest", help="Importa eventos JSON Lines")
    p.add_argument("file")
    sub.add_parser("detect", help="Executa regras de detecção")
    sub.add_parser("report", help="Exibe resumo e alertas")
    args = parser.parse_args()
    if args.command == "ingest": ingest(args.file)
    elif args.command == "detect": detect()
    else: report()

if __name__ == "__main__":
    main()
