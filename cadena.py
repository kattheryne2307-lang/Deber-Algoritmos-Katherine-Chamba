#Invertir una cadena usando pila
def invertir_cadena(cadena):
    pila=[]
    for caracter in cadena:
        pila.append(caracter)
    invertida=""
    while len(pila)>0:
        invertida += pila.pop()
    return invertida

cadena=input("Ingrese una cadena: ")
print("La cadena invertida es: ",invertir_cadena(cadena))