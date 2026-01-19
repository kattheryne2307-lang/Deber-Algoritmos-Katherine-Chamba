def es_palindromo(palabra):
    pila=[]
    for letra in palabra:
        pila.append(letra)
    reverso=""
    while len(pila)>0:
        reverso=pila.pop()
    return palabra==reverso

palabra="oso"
print(es_palindromo(palabra))