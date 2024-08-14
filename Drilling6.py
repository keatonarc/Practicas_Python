#Drilling 6 determinar 3 numeros
numero1 = int(input("Ingrese un numero:"))
numero2 = int(input("Ingrese un numero:"))
numero3 = int(input("Ingrese un numero:"))
#Calculo
if numero1 > numero2 and numero1 > numero3:
    print("El numero mayor es:",numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("El numero mayor es:", numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("El numero mayor es:", numero3)
else:
    print("No se puedo establecer el numerop Mayor")