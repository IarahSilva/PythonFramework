class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir(no.direita, valor)

    def buscar(self, no, valor):
        if no is None or no.valor == valor:
            return no

        if valor < no.valor:
            return self.buscar(no.esquerda, valor)

        return self.buscar(no.direita, valor)


arvore = Arvore()

for numero in [50, 30, 70, 20, 40, 60, 80]:
    arvore.inserir(numero)

resultado = arvore.buscar(arvore.raiz, 40)

print("Encontrado!" if resultado else "Não encontrado!")