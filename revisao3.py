a = input("Informe um valor para a: ")
b = input("Informe um valor para b: ")

print("ANTES: O valor de a eh", a, "e o valor de b eh", b)

auxiliar=a
a = b
b = auxiliar
print("DEPOIS: O valor de a eh", a, "e o valor de b eh", b)
