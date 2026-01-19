with open("saludo.txt","w") as f:
    f.write("Hola Mundo\n")
    f.write("Hola Python\n")
    f.write("Hola Katherine\n")

with open("saludo.txt","r") as f:
    for linea in f:
        print(linea.strip())

try:
    with open("registro.txt","x") as f:
        f.write("Registro inicial\n")
except FileExistsError:
    print("Error: registro.txt ya existe")

with open("saludo.txt","r") as f:
    print(len(f.readlines()))

with open("saludo.txt","r") as f1, open("copia_saludo.txt","w") as f2:
    f2.write(f1.read())

with open("saludo.txt","a") as f:
    f.write("Nueva línea agregada\n")

with open("saludo.txt","r") as f:
    texto=f.read()
    print(texto.count("Python"))

with open("saludo.txt","r") as f:
    for linea in f:
        if "Hola" in linea:
            print(linea.strip())

nombres=["Ana","Luis","Pedro","Katherine"]
with open("nombres.txt","w") as f:
    for n in nombres:
        f.write(n+"\n")

with open("nombres.txt","r") as f:
    for linea in f:
        print(linea.strip().upper())

with open("datos.txt","w") as f:
    f.write("Primera línea\nSegunda línea\nTercera línea\n")

with open("datos.txt","r") as f:
    for linea in f:
        print(linea.strip())

with open("datos.txt","r") as f:
    print(len(f.readlines()))

with open("datos.txt","a") as f:
    f.write("Cuarta línea\n")

with open("datos.txt","r") as f:
    for linea in f:
        if "línea" in linea:
            print(linea.strip())

with open("datos.txt","r") as f1, open("copia_datos.txt","w") as f2:
    f2.write(f1.read())

nombre=input("Nombre del archivo: ")
texto=input("Texto: ")
with open(nombre,"w") as f:
    f.write(texto+"\n")

with open("mensajes.txt","w") as f:
    while True:
        linea=input("Escribe: ")
        if linea.lower()=="salir":
            break
        f.write(linea+"\n")

nombre=input("Archivo a leer: ")
with open(nombre,"r") as f:
    for linea in f:
        print(linea.strip())

with open("nombres.txt","w") as f:
    while True:
        nombre=input("Nombre (salir para terminar): ")
        if nombre.lower()=="salir":
            break
        f.write(nombre+"\n")

def cargar():
    try:
        with open("personas.txt","r") as f:
            return [linea.strip() for linea in f]
    except FileNotFoundError:
        return []

def guardar(lista):
    with open("personas.txt","w") as f:
        for p in lista:
            f.write(p+"\n")

personas=cargar()
while True:
    print("1. Crear\n2. Listar\n3. Actualizar\n4. Eliminar\n5. Salir")
    op=input("Opción: ")
    if op=="1":
        nombre=input("Nombre: ")
        personas.append(nombre)
        guardar(personas)
    elif op=="2":
        for i,p in enumerate(personas):
            print(i,p)
    elif op=="3":
        i=int(input("Índice: "))
        if 0<=i<len(personas):
            personas[i]=input("Nuevo nombre: ")
            guardar(personas)
    elif op=="4":
        i=int(input("Índice: "))
        if 0<=i<len(personas):
            personas.pop(i)
            guardar(personas)
    elif op=="5":
        break

usuarios={"admin":"1234"}
personas={}
def login():
    u=input("Usuario: ")
    c=input("Clave: ")
    return usuarios.get(u)==c
def menu():
    while True:
        print("1. Crear\n2. Listar\n3. Actualizar\n4. Eliminar\n5. Salir")
        op=input("Opción: ")
        if op=="1":
            dni=input("DNI: ")
            nombre=input("Nombre: ")
            personas[dni]=nombre
        elif op=="2":
            for k,v in personas.items():
                print(k,v)
        elif op=="3":
            dni=input("DNI: ")
            if dni in personas:
                personas[dni]=input("Nuevo nombre: ")
        elif op=="4":
            dni=input("DNI: ")
            if dni in personas:
                del personas[dni]
        elif op=="5":
            break
if login():
    menu()
else:
    print("Login incorrecto")

def quicksort_inplace(lista,inicio,fin):
    if inicio<fin:
        p=particion(lista,inicio,fin)
        quicksort_inplace(lista,inicio,p-1)
        quicksort_inplace(lista,p+1,fin)
def particion(lista,inicio,fin):
    pivote=lista[fin]
    i=inicio-1
    for j in range(inicio,fin):
        if lista[j]<=pivote:
            i+=1
            lista[i],lista[j]=lista[j],lista[i]
    lista[i+1],lista[fin]=lista[fin],lista[i+1]
    return i+1
datos=[8,3,1,7,0,10,2]
quicksort_inplace(datos,0,len(datos)-1)
print(datos)

def merge_sort(lista):
    if len(lista)<=1:
        return lista
    medio=len(lista)//2
    izquierda=merge_sort(lista[:medio])
    derecha=merge_sort(lista[medio:])
    return merge(izquierda,derecha)
def merge(izq,der):
    resultado=[]
    i=j=0
    while i<len(izq) and j<len(der):
        if izq[i]<=der[j]:
            resultado.append(izq[i]); i+=1
        else:
            resultado.append(der[j]); j+=1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado
print(merge_sort([8,3,1,7,0,10,2]))