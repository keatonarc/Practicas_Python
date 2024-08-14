#crear una lista de 10 numeros enteros, recorrerla con .for, imprimir en pantalla el valor de cada elemento si es par o impar o cero
lista=[10,15,50,1,5,3,7,8,9,2]
for lista in lista:
    if lista % 2 == 0:
        print(lista, "es par.")
    elif lista % 2 == 1:
        print(lista, "es impar.")