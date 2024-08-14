#Drilling 9 calculadora
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Error")
    return a / b

def calcular_operaciones(a, b):
#resultados definicion   
    resultados = {
        'Suma': sumar(a, b),
        'Resta': restar(a, b),
        'Multiplicación': multiplicar(a, b),
        'División': dividir(a, b)
    }
    return resultados
#uso
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultados = calcular_operaciones(num1, num2)
    
    print("\nResultados:")
    for operacion, resultado in resultados.items():
        print(f"{operacion}: {resultado}")
except ValueError as e:
    print(f"Error: {e}")