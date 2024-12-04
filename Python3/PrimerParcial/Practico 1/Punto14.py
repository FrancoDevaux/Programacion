"""
Escriba un programa que dado un texto ingresado por el usuario cuente 
la cantidad total de vocales que aparecen y lo muestre por pantalla.
"""

texto = input("\nIngrese una cadena: ")
vocales = "aeiouàèìòùáéíóú"
contador = 0

for letra in texto:
    if letra.lower() in vocales:
        contador += 1

print(f"\nLa cantidad de vocales de {texto} es de ---> {contador}")

