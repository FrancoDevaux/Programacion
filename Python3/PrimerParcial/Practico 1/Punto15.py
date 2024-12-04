"""
Escriba un programa que, dada una oración ingresada muestre por pantalla:
a)El número total de caracteres en la oración
b)La cantidad total de letras (consonantes y vocales, sin signos de puntuación)
c)La cantidad de palabras separadas por uno o más espacios
En este ejercicio, para simplificar, asumiremos que los posibles caracteres de entrada son letras, 
espacios, dígitos, signos de puntuación, signos de interrogación y de exclamación.
Investigar si hay funciones de strings que nos faciliten la resolución [len(), .isalpha(), .split() , etc.]
"""

import string

oracion = input("\nIngrese una oracion: ")


#A)Total de caracteres
print(f"\n[+]La oracion tiene {len(oracion)} caracteres")


#B)Total de vocales y consonantes sin puntuacion
oracion_sin_puntuacion = oracion.translate(str.maketrans('', '', string.punctuation)) # Eliminar signos de puntuación
#El método translate() se utiliza para reemplazar caracteres en una cadena de texto
#str.maketrans() crea una tabla de traducción.
#Los tres argumentos vacíos al principio indican que no se reemplazarán ningún carácter.
#El tercer argumento, string.punctuation, es una cadena que contiene todos los signos de puntuación comunes. 
# Al pasarlo como tercer argumento, se indica que todos los caracteres presentes en string.punctuation 
# deben ser eliminados de la cadena original.
#string.punctuation: Esta variable contiene una cadena con los siguientes caracteres: (!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`.)



# Inicializar contadores
cantidad_letras = 0
cantidad_vocales = 0
cantidad_consonantes = 0

for letra in oracion_sin_puntuacion:
    if letra.isalpha():  # Verificar si es una letra
        cantidad_letras += 1
        if letra.lower() in "aeiouáéíóú":
            cantidad_vocales += 1
        else:
            cantidad_consonantes += 1

print("\nLa oración tiene:")
print("- Un total de", cantidad_letras, "letras.")
print("- Un total de", cantidad_vocales, "vocales.")
print("- Un total de", cantidad_consonantes, "consonantes.")


#C)Total de palabras separadas
palabras = oracion.split()  #slip te cuenta la cant de palabras separadas por espacios
print(f"\n[+]La oración tiene {len(palabras)} palabras.")