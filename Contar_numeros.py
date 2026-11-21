num = int(input("Ingrese un numero: "))
cont = 0

while num != 0:
    if num > 0:
        cont += 1
        num = int(input("Ingrese un numero: "))

print("La cantidad de numeros ingresados es: "+str(cont))
