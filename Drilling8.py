#lista
lista = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]

#arranque del diccionario
diccionario = {}

#recorrer las sublistas
for i, sublista in enumerate(lista):
    # Verificar si es 0
    if sublista[0] == 0:
        continue  
    
    #imprimir los números de la sublista sin los 0s
    for numero in sublista:
        if numero != 0:
            print(numero, end=' ')
    print()

#diccionario A, B, C, D
claves = ['A', 'B', 'C', 'D']
for i, sublista in enumerate(lista):
    if sublista[0] != 0: 
        diccionario[claves[i]] = sublista

# imprimir el diccionario
print("\nDiccionario resultante:")
print(diccionario)