a = (int)(input("Digite valor para 'a': "))
b = (int)(input("Digite valor para 'b': "))
c = (int)(input("Digite valor para 'c': "))
delta = b**2 -4*a*c
x1 = -b + delta**(1/2)/2*a
x2 = -b - delta**(1/2)/2*a

print(x1,x2)
