"""
Escriba un programa que para un texto ingresado nos muestre cual es la palabra más larga 
dentro de ese texto y cuántas letras tiene.
"""

texto = input("\nIngrese un texto: ")

palabras = texto.split() #esta función es dividir una cadena en una lista de subcadenas, 
                         #utilizando los espacios en blanco como separadores. 

palabra_mas_larga = max(palabras, key=len)
#max() compara los elementos de la lista según su orden natural, es decir, de menor a mayor.
#key=len:El argumento key le indica a max() que en lugar de comparar los elementos directamente, 
#debe aplicar la función especificada (en este caso, len) a cada elemento antes de realizar la comparación.
#Al especificar key=len, le decimos a max() que en lugar de comparar las palabras directamente, compare sus longitudes.


#Imprimirlo por consola
print(f"\nLa palabra más larga es: {palabra_mas_larga}")
print(f"La palabra tiene {len(palabra_mas_larga)} letras")