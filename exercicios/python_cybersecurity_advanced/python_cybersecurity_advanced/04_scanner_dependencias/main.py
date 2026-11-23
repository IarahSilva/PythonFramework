import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

def run_audit(requirements, output):
    if not Path(requirements).is_file():
        raise SystemExit(f"Arquivo não encontrado: {requirements}")
    if not shutil.which("pip-audit"):
        raise SystemExit("pip-audit não encontrado. Instale com: python -m pip install pip-audit")
    command = [
        "pip-audit",
        "--requirement", requirements,
        "--format", "json"
    ]
    print("Executando:", " ".join(command))
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.stdout.strip():
        try:
            data = json.loads(result.stdout)
            Path(output).write_text(json.dumps(data, indent=2), encoding="utf-8")
            print(f"Relatório JSON salvo em: {output}")
            vulnerabilities = []
            for dependency in data:
                for vuln in dependency.get("vulns", []):
                    vulnerabilities.append((dependency.get("name"), dependency.get("version"),
                                             vuln.get("id"), vuln.get("fix_versions", [])))
            print("\n=== RESUMO ===")
            print("Dependências avaliadas:", len(data))
            print("Vulnerabilidades encontradas:", len(vulnerabilities))
            for name, version, vuln_id, fixes in vulnerabilities:
                print(f"- {name} {version}: {vuln_id}; correções: {', '.join(fixes) or 'não informadas'}")
        except json.JSONDecodeError:
            print("Não foi possível interpretar o JSON retornado.")
            print(result.stdout[:2000])
    if result.stderr.strip():
        print("\nMensagens:", result.stderr.strip())
    if result.returncode not in (0, 1):
        raise SystemExit(f"pip-audit terminou com código {result.returncode}")

def main():
    parser = argparse.ArgumentParser(description="Audita dependências Python com pip-audit.")
    parser.add_argument("-r", "--requirements", default="requirements-audit.txt")
    parser.add_argument("-o", "--output", default="audit-report.json")
    args = parser.parse_args()
    run_audit(args.requirements, args.output)

if __name__ == "__main__":
    main()
