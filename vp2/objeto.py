#pessoa1 = ["adamor","065-054-343-21", "adamorhenner2@outlook.com"]
#pessoa2 = ["adam", "123456894", "ada_candido@hotmail.com"]

#print(pessoa1[0], pessoa1[1], pessoa1[2])


p1 = {'nome': 'Adamor', 'cpf': '06505434321', 'email': 'adamorhenner2@outlook.com'}
p2 = {'nome': 'Adamor1', 'cpf': '06505434321', 'email': 'adamorhenner2@outlook.com'}
p3 = {'nome': 'Adamor2', 'cpf': '06505434321', 'email': 'adamorhenner2@outlook.com'}
p4 = {'nome': 'Adamor3', 'cpf': '06505434321', 'email': 'adamorhenner2@outlook.com'}
p5 = {'nome': 'Adamor4', 'cpf': '06505434321', 'email': 'adamorhenner2@outlook.com'}
p6 = {'nome': 'Adamor5', 'cpf': '06505434321', 'email': 'adamorhenner2@outlook.com'}
p7 = {'nome': 'Adamor6', 'cpf': '06505434321', 'email': 'adamorhenner2@outlook.com'}

print(p1['nome'], p1['cpf'], p1 ['email'])

pessoas = []
pessoas.append(p1)
pessoas.append(p2)
pessoas.append(p3)
pessoas.append(p4)
pessoas.append(p5)
pessoas.append(p6)
pessoas.append(p7)

for pessoa in pessoas:
    print(pessoa['nome'])