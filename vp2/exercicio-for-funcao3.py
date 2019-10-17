#crie uma funcao que recebe um texto
#e retorna verdadeiro,  caso ele seja palindromo
#ou falso, caso nao seja palindromo
#Teste a funcao ao final do codigo
def ehPalidromo(texto):
    textoAoContrario = ""

    for letra in texto:
        textoAoContrario = letra + textoAoContrario

    if texto == textoAoContrario:
        return True
    else:
        return False

print(ehPalidromo("omo"))
print(ehPalidromo("apos a sopa"))
print(ehPalidromo("a sacada da casa"))