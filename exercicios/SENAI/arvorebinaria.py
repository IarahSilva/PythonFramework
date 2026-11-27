# Classe que representa cada nó da árvore
class No:

    # Inicializa um novo nó com seu valor
    def __init__(self, valor):
        self.valor = valor

        # Define os filhos esquerdo e direito inicialmente como vazios
        self.esquerda = None
        self.direita = None


# Classe responsável por organizar e manipular a árvore
class Arvore:

    # Inicializa a árvore sem nenhum elemento
    def __init__(self):
        self.raiz = None

    # Método responsável por inserir um novo valor na árvore
    def inserir(self, valor):

        # Verifica se a árvore está vazia
        if self.raiz is None:

            # Se estiver vazia, o novo nó será a raiz
            self.raiz = No(valor)

        else:
            # Se já existir uma raiz, chama o método auxiliar
            self._inserir(self.raiz, valor)

    # Método recursivo que encontra a posição correta para inserir o valor
    def _inserir(self, no, valor):

        # Se o valor for menor que o nó atual, vai para a esquerda
        if valor < no.valor:

            # Verifica se o lado esquerdo está vazio
            if no.esquerda is None:

                # Insere o novo nó à esquerda
                no.esquerda = No(valor)

            else:
                # Se já existir um nó, continua procurando recursivamente
                self._inserir(no.esquerda, valor)

        else:
            # Se o valor for maior ou igual, vai para a direita
            if no.direita is None:

                # Insere o novo nó à direita
                no.direita = No(valor)

            else:
                # Se já existir um nó, continua procurando recursivamente
                self._inserir(no.direita, valor)

    # Método responsável por buscar um valor na árvore
    def buscar(self, no, valor):

        # Caso base: retorna None se o nó estiver vazio
        # ou retorna o nó se o valor procurado for encontrado
        if no is None or no.valor == valor:
            return no

        # Se o valor procurado for menor, busca na esquerda
        if valor < no.valor:
            return self.buscar(no.esquerda, valor)

        # Caso contrário, busca na direita
        return self.buscar(no.direita, valor)


# Cria uma nova árvore vazia
arvore = Arvore()


# Insere os valores na árvore
for numero in [50, 30, 70, 20, 40, 60, 80]:
    arvore.inserir(numero)


# Busca o valor 40 começando pela raiz
resultado = arvore.buscar(arvore.raiz, 40)


# Verifica se o valor foi encontrado e exibe a mensagem
print("Encontrado!" if resultado else "Não encontrado!")