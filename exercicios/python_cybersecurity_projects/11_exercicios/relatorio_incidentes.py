import json
from datetime import datetime
from html import escape


incidentes = []


def registrar():
    print("\nNOVO INCIDENTE")

    incidente = {
        "id": len(incidentes) + 1,
        "data": datetime.now().isoformat(
            timespec="seconds"
        ),
        "tipo": input("Tipo do incidente: "),
        "gravidade": input("Gravidade: "),
        "descricao": input("Descrição: "),
        "status": "Em análise"
    }

    incidentes.append(incidente)

    print("Incidente registrado!")


def salvar_json():
    with open(
        "incidentes.json", "w", encoding="utf-8"
    ) as arquivo:
        json.dump(
            incidentes,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def gerar_html():
    linhas = ""

    for incidente in incidentes:
        linhas += f"""
        <tr>
            <td>{incidente['id']}</td>
            <td>{escape(incidente['data'])}</td>
            <td>{escape(incidente['tipo'])}</td>
            <td>{escape(incidente['gravidade'])}</td>
            <td>{escape(incidente['descricao'])}</td>
            <td>{escape(incidente['status'])}</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Relatório de Segurança</title>
        <style>
            body {{ font-family: Arial; padding: 20px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ccc; padding: 10px; }}
            th {{ background: #222; color: white; }}
        </style>
    </head>
    <body>
        <h1>Relatório de Incidentes</h1>
        <table>
            <tr>
                <th>ID</th><th>Data</th><th>Tipo</th>
                <th>Gravidade</th><th>Descrição</th><th>Status</th>
            </tr>
            {linhas}
        </table>
    </body>
    </html>
    """

    with open(
        "relatorio.html", "w", encoding="utf-8"
    ) as arquivo:
        arquivo.write(html)


def main():
    while True:
        print("\n1 - Registrar incidente")
        print("2 - Gerar relatórios")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            registrar()

        elif opcao == "2":
            salvar_json()
            gerar_html()
            print("Relatórios gerados!")

        elif opcao == "0":
            break


if __name__ == "__main__":
    main()

#1 - Registrar incidente

#[NOVO INCIDENTE]
#Tipo do incidente: Acesso não autorizado
#Gravidade: Alta
#Descrição: Tentativas suspeitas de login

#Incidente registrado!

# 2 - Gerar relatórios

#Relatórios gerados!