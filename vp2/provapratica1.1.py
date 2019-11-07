x = 0
pergunta = input("Impar ou par ?")
while x <= 100:
    if pergunta == "par" and x %2 == 0 :
        print(x)
    elif pergunta == "impar" and x %2 != 0:
        print (x)
    x = x +1
