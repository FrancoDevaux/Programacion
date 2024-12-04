"""Escriba un programa que permita leer de un archivo distancias.txt (cada renglón
tiene una distancia válida) las distancias recorridas por el vehículo de una empresa,
luego calcular cual es la distancia promedio, y mostrar por pantalla el promedio y
todas las distancias mayores al promedio.
Ej del contenido del archivo:
150
120
50
34
250
Salida: “La distancia promedio de los viajes es … y los viajes con distancia mayor
son: … , … , …. , …. “
"""

def mostrar_Promedio_Mayor(archivo_distancias):

    #Abrimos el archivo en modo lectura. El bloque 'with' asegura que el archivo se cierre
    with open(archivo_distancias, 'r') as f:

        #Crreamos una lista llamda 'distancia' para almacenar valores numericos
        #'linea.strip' elimina espacios en blanco al principio y final
        #'float' convierte la linea (que es texto) en un nùmero de punto flotante
        distancia = [float(linea.strip()) for linea in f]

    #Usar linea.strip para los espacio en bakncos porque sino da probelmas

    #Suma todos los elemtos de la lista distancia y con 'len' cuenta el numero de elementos en la lista
    promedio = sum(distancia) / len(distancia) 



    #Se cre una nueva lista llamada 'mayores'
    #Para cada distancias en la lista 'distancia'
    #si la distancias es mayor que promedio, se agrega a la lista 'mayor'
    mayor = [distancias for distancias in distancia if distancias > promedio]


    #':.2f' el promedio con dos decimales
    print(f"\nLa distacia promedio de los viajes es {promedio:.2f} y los viajes con distancia mayor son: {mayor}")


if __name__ == "__main__":
    mostrar_Promedio_Mayor("C:/Users/FRANCO/Desktop/Python3/PrimerParcial/Practico 2/distancias.txt")