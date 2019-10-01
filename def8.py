def BrToEua(notabr):
    if nota < 5.0:
        return "D"
    elif nota < 7.0:
        return "C"
    elif nota < 9.0:
        return "B"
    else:
        return "A"


print("Calculo o conceito americano baseado na sua nota brasileira")

nota = (float) (input("Digite sua nota"))
conceito = BrToEua(nota)

print("Parabens, seu conceito eh", conceito )
