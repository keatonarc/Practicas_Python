#estructura de datos
estudiantes = [
 {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
 {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
 {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
 {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
 {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
 ]
#calculo numero primos
def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
#calculo de promedio
def promedio_calificaciones(calificaciones):

    return sum(calificaciones) / len(calificaciones)

#filtro de estudiantes
estudiantes_filtrados = [
    estudiante for estudiante in estudiantes
    if estudiante['edad'] > 18 and promedio_calificaciones(estudiante['calificaciones']) > 85
]

print("Estudiantes filtrados:")
for estudiante in estudiantes_filtrados:
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Calificaciones: {estudiante['calificaciones']}")

#calculo para las notas de estudiantes +18
estudiantes_primos = [
    estudiante for estudiante in estudiantes
    if estudiante['edad'] > 18 and es_primo(estudiante['edad'])
]

promedios_primos = [promedio_calificaciones(estudiante['calificaciones']) for estudiante in estudiantes_primos]

if promedios_primos:
    promedio_general_primos = sum(promedios_primos) / len(promedios_primos)
    print(f"\nPromedio general de calificaciones para estudiantes con edad numero primo: {promedio_general_primos:.2f}")
else:
    print("\nNo hay estudiantes que cumplan con el criterio.")