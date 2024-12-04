"""
Escriba un programa que permita cargar una lista de alumnos junto con su nota del
parcial. Seleccione la estructura de datos que mejor se adapte al problema. Luego
de ingresados los datos debe generar una lista donde figure si aprobaron o no (se
aprueba con 40 o más). El listado a mostrar por pantalla debe ser como el siguiente
(el resultado no se almacena, se calcula):

ALUMNOS             PARCIAL                     RESULTADO
Smith,Juan            70                         Aprobado
Suárez, María         35                         Desaprobado
"""

#Creamos una variable vacia que almacena los datos de cada alumno
alumnos = []

#Cargar datos
while True:
    nombre = input("\nIngrese el nombre del alumno (o 'fin' para terminar): ")

    if nombre.lower() == 'fin':
        break

    nota = int(input("Ingrese nota del parcial: "))
    alumnos.append((nombre, nota))


#Mostrar resultados
print("Alumnos\tParcial\tResultado")

#Recorrer el elemento
for nombre,nota in alumnos:
    resultado = "Aprobado" if nota >= 40 else "Desaprobado"
    print(f"{nombre}\t{nota}\t{resultado}")

