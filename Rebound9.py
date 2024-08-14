def calcular_area_rectangulo(base, altura):
    
    if not (isinstance(base, (int, float)) and isinstance(altura, (int, float))):
        raise ValueError("Base y altura deben ser números.")
    
    if base <= 0 or altura <= 0:
        raise ValueError("Base y altura deben ser números positivos.")

    area = base * altura
    return area

try:
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = calcular_area_rectangulo(base, altura)
    print(f"El área del rectángulo es: {area}")
except ValueError as e:
    print(f"Error: {e}")