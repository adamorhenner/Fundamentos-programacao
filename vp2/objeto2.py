class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

p1 = Pessoa("adamor","065054343", "adamorhenner2@outlook.com")
p2 = Pessoa("adamo","06505434", "adamohenner2@outlook.com")
p3 = Pessoa("adam","0650543", "adamhenner2@outlook.com")
p4 = Pessoa("ada","065054", "adahenner2@outlook.com")

print(p1.nome, p1.cpf, p1.email)

p = []
p.append(p1)
p.append(p2)
p.append(p3)
p.append(p4)

for pessoa in p:
    print(pessoa.nome, pessoa.cpf, pessoa.email)