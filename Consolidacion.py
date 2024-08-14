#lista de nombres
nombres = [
    'Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi',
    'Teller', 'Einstein', 'Pele', 'Juanes'
]
#categorias
magos = {'Harry Houdini', 'David Blaine', 'Teller'}
cientificos = {'Newton', 'Hawking', 'Einstein'}
#funcion para separar
def separar_nombres(nombres):
    magos_lista = []
    cientificos_lista = []
    otros_lista = []

    for nombre in nombres:
        if nombre in magos:
            magos_lista.append(nombre)
        elif nombre in cientificos:
            cientificos_lista.append(nombre)
        else:
            otros_lista.append(nombre)
    
    return magos_lista, cientificos_lista, otros_lista

#funcion para modificar magos
def hacer_grandioso(magos_lista):
    return ['El gran ' + nombre for nombre in magos_lista]
#funcion para imprimir
def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)
#separacion de listas
magos_lista, cientificos_lista, otros_lista = separar_nombres(nombres)
#impresion lista completa
print("Lista completa de nombres:")
imprimir_nombres(nombres)
#modifuicar magos
magos_grandiosos = hacer_grandioso(magos_lista)
print("\nMagos grandiosos:")

imprimir_nombres(magos_grandiosos)

print("\nCientíficos:")
imprimir_nombres(cientificos_lista)

print("\nOtros:")

imprimir_nombres(otros_lista)