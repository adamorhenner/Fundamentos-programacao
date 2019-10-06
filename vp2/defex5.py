def media(nota, nota2, nota3):
    return (nota + 2 * nota2 + 3 * nota3) / 6


print("-----calculo da media-------")
vp= (float)(input("valor da vp1: "))
vp2= (float)(input("valor da vp2: "))
vf= (float)(input("valor da vf: "))

media = media(vp, vp2, vf)
print("Sua media eh:", media)
