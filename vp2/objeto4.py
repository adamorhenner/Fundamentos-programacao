class Calculadora:
    def __init__(self):
        self.valores = []

    def proximoValor(self, valor):
        self.valores.append(valor)

    def somar(self):
        soma = 0

        for valor in self.valores:
            soma += valor
        
        return soma

    def multiplicar(self):
        multiplicar = 1

        for valor in self.valores:
            produto = multiplicar * valor

        return produto

#c = Calculadora()
#c.proximoValor(10)
#c.proximoValor(20)
#c.proximoValor(30)

#print(c.somar())

valor = 0
c = Calculadora()

while (True):
    valor = int(input("Digite um valor para ser multiplicar: "))
    c.proximoValor(valor)

    decisao = input('Deseja continuar(S/N)?: ')

    if decisao == "N":
        break
    
print("O valor da soma eh: ", c.multiplicar())