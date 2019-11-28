class Heroi:
    def __init__(self, poder, nome):
        self.poder = poder
        self.nome = nome

    def usarPoder(self):
        print(self.nome, " esta usando o poder ", self.poder )

h1 = Heroi("Batman", "Dinheiro")
h2 = Heroi("Fenix", "Flopar")


h1.usarPoder()
h2.usarPoder()