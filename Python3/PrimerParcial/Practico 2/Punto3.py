"""Escriba un programa que permita cargar las notas de exámenes, primero debe
permitir ingresar por teclado la cantidad de notas que desea cargar, y luego
cargarlas en una lista, y posteriormente debe buscar la nota más alta, mostrarla, e
indicar en qué índice del arreglo se encuentra
"""


def cargarNotas():
    cantidad_notas = int(input("\nIngrese cuantas notas desea cargar: "))
    notas = [] #Declaramos un alista vacia

    for i in range(cantidad_notas):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    
    return notas

def nota_mas_alta(notas):
    nota_alta = max(notas)
    indice = notas.index(nota_alta)
    #El método index() se utiliza para encontrar la posición de un elemento específico dentro de una lista. 
    #En otras palabras, te dice en qué lugar (índice) de la lista se encuentra el elemento que estás buscando.


    return nota_alta, indice  #Que me retorn las dos variables

def main():
    notas = cargarNotas()
    nota_alta, indice = nota_mas_alta(notas)

    print(f"\n[+]La nota mas alta es: {nota_alta}, se encuentra en el inidce: {indice}")


if __name__ == "__main__":
    main()