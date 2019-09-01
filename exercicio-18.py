print("==MEDIA==")
vp = (float)(input("Qual nota da sua vp? "))
vp2 = (float)(input("Qual nota da sua vp2? "))
vf = (float)(input("Qual nota da sua vf? "))
media = (vp+2*vp2+3*vf)/6
if media>=5.5:
    print("APROVADO!")
else:
    print("REPROVADO!")
