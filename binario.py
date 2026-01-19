#convertir un numero decimal a binario

def decimal_a_binario(numero):
    pila=[]
    while numero>0:
        residuo=numero % 2
        pila.append(str(residuo))
        numero=numero//2
    binario=""
    while len(pila) >0:
        binario += pila.pop()
    return binario

decimal = int(input("Ingrese un número decimal: "))
print("El numero decimal ",decimal,"convertido a binario es: ", decimal_a_binario(decimal))