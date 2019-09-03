print("===Verificar temperatura===")
tipo = input("Diga qual tipo de temperatura? ")
temperatura=(float)(input("Digite o valor da temperatura: "))
if tipo =="C":
    print((temperatura-32)/1.8)
else:
    print(temperatura*1.8+32)

#professor
print("=== CONVERSOR DE TEMPERATURA ===")

temperatura = (float)(input("Digite um valor para temperatura "))
tipo = input("Digite C para celsius e F para Farenheit ")

resultado = 0.0

if tipo == "C" or "c":
    resultado = temperatura * 1.8 + 32
    print( temperatura, "ºC em Farenheit eh", resultado, "ºF")
elif tipo == "F" or "f":
    resultado = (temperatura - 32)/ 1.8
    print(temperatura, "ºF em Celsius eh", resultado, "ºC")
else:
    print("Vc digitou um valor nao correspondente")