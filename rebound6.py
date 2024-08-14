#Rebound 6 if

#ingresar numero
numero=int(input("ingresa un numero:"))

#if positivo
if  numero<0:
    print(numero,"es negativo")
elif numero>0:
    print(numero,"es positivo")
if numero % 2 == 0:
    print(numero, "es par.")
elif numero % 2 == 1:
    print(numero, "es impar.")
else:
    print("el numero es 0")
