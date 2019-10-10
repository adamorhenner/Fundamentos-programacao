print("Esse programa calcula os valores possiveis de x, baseado")

a = (float)(input("Digite valor para 'a': "))
b = (float)(input("Digite valor para 'b': "))
c = (float)(input("Digite valor para 'c': "))

#calcula o valor do delta
delta = b**2 -4*a*c

#calcula o valor de x com delta positivo
x1 = (-b + (delta**(1/2)))/2*a

#calcula o valor de x com delta negativo
x2 = (-b - (delta**(1/2)))/2*a

print("Os valores possiveis de x são ", x1,x2)
