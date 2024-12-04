"""Un profesor almacenó los datos de los alumnos de su materia en un archivo
alumnos.txt. En cada línea guardó el número de legajo del alumno y sus tres notas
finales (oral, escrito y trabajos prácticos). El archivo está ordenado por número de legajo.
En otro archivo, ordenado alfabéticamente por apellido, guarda por línea, número de
legajo, apellido y nombre de cada uno.
En ambos archivos los datos están separados por punto y coma ( ; ) .
Desea escribir un programa para generar un archivo Promoción.txt con los apellidos
y nombres de los alumnos que promocionan la materia, esto es, 
alumnos que el promedio de las tres notas supere los 7 puntos.
El archivo debe quedar ordenado alfabéticamente
"""

#Abrimos los archivos
ruta_nombre = open("PrimerParcial/Practico 2/nombres.txt", "r")
ruta_alumnos = open("PrimerParcial/Practico 2/alumnos.txt", "r")
ruta_promocion = open("PrimerParcial/Practico 2/promocion.txt", "w")


#Almacenar los legajos que los promedio de las 3 notas den mas de 7

lista_promedio = []

for linea in ruta_alumnos:
    lista = linea.strip().split(";")   #Me saca los esapcio y me devuelve una lista

    if ((float(lista[1]) + float(lista[2]) + float(lista[3])) / 3) >= 7:
        lista_promedio.append(lista[0])   #Me hace el append del legajo que esta en posicion cero del alumnos.txt

for linea in ruta_nombre:
    lista = linea.strip().split(";")

    if lista[0] in lista_promedio:
        ruta_promocion.write(f"{lista[1]}:{lista[2]} \n")


#Cerramos los archivos
ruta_alumnos.close()
ruta_nombre.close()
ruta_promocion.close()