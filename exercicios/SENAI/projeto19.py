#Arquivo para a criação de times de esportes. Que podem ser futebol, volei e basquete.

class Clubes:    #Atributos == característica do objeto
    def __init__(self, nome:str, fundacao:int, corUniforme:str, mascote:str, modalidade:str):
        self.nome = nome
        self.fundacao = fundacao
        self.corUniforme = corUniforme #Dados Externos
        self.mascote = mascote
        self.modalidade = modalidade
        self.campeonatos = 6
        self.jogos = 0
        self.vitorias = 0
        self.derrotas = 0
    
    #Métodos == ações do objeto
    def ganhar(self):
        self.vitorias += 1


    def jogar(self):
        self.jogos += 1


    def perder(self):
        self.derrotas += 1

    def trocarUniforme(self):
        pass

time1 = Clubes("São Paulo", 1930, "Branco", "Santo Paulo", "Futebol")
time2 = Clubes("Capivariano", 1918, "Vermelho", "Leão", "Futebol")
time3 = Clubes("Palmeiras", 1800, "Verde", "Porco", "Futebol")
time4 = Clubes("Flamengo", 1895, "Vermelho", "Urubu", "Futebol")
time5 = Clubes("Fúria", 2017,"Preto", "Pantera", "CS2")

time1.jogar()
time2.jogar()
time1.perdeu()
time2.ganhar()

print(f"O time {time1.nome} tem {time1.vitorias} vitórias \
e {time1.derrotas} derrotas.")
print(f"O time {time2.nome} tem {time2.vitorias} vitórias \
e {time2.derrotas} derrotas.")

print()
