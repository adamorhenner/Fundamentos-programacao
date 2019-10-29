cidades = ["caninde", "chorozinho", "Juazeiro"]
horarios = ["11:00","12:00", "19:00", "22:00"]

print("Qual seu destino?")
opcao = 1

for cidade in cidades:
    print("Digite ", opcao," para ", cidade)
    opcao = opcao+1
    cidadeEscolhida = (int)(input())
cidades[0]
opcao = 1
print ("Escolha o horario")
for horario in horarios:
    if horario == "11:00" or horario == "12:00":
        if cidadeEscolhida == 1 :
            valor = 30
        elif cidadeEscolhida == 2 :
            valor = 10
        elif cidadeEscolhida == 3 :
            valor = 100
    elif horario == "19:00" or horario == "22:00":
        if cidadeEscolhida == 1:
            valor = 50
        elif cidadeEscolhida == 2 :
            valor = 20
        elif cidadeEscolhida == 3 :
            valor = 140
    print("digite ", opcao, " para ",  horario ,"(R$ ", valor,")")
    horarioEscolhido = (int)(input())
    opcao= opcao + 1
data = input("Informe a data: ")
quantidadeDePessoas = (int)(input("Quantas pessoas: "))
#Calculo do valor
    if horarioEscolhido == 1 or horarioEscolhido == 2 :
        if cidadeEscolhida == 1
            valor = 30
        elif cidadeEscolhida == 2 :
            valor = 10
        elif cidadeEscolhida == 3 :
            valor = 100
    elif horarioEscolhido == 3 or horarioEscolhido == 4 :
        print("Confira seus dados")
        print("Destino ", cidade[cidadeEscolhida - 1])
        print("Data: ", data)
        print("Horario: ", horario[horarioEscolhido - 1])
        print("Valor total: ", valor * quantidadeDePessoas)
