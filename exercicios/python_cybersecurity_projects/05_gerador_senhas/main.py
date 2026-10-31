import argparse, secrets, string

def gerar(tamanho):
    if tamanho < 12: raise ValueError("Use no mínimo 12 caracteres.")
    grupos = [string.ascii_lowercase, string.ascii_uppercase, string.digits, "!@#$%&*-_+"]
    chars = [secrets.choice(g) for g in grupos]
    todos = "".join(grupos)
    chars += [secrets.choice(todos) for _ in range(tamanho - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--tamanho", type=int, default=16)
    a = p.parse_args()
    try: print(gerar(a.tamanho))
    except ValueError as e: p.error(str(e))
