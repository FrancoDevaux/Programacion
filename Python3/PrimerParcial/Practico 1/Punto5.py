"""
Dada una cadena de texto ingresada por consola, decir cuántos “espacios” contiene.
"""

texto = input("\nIngrese un cadena de texto: ")
contador = 0

for caracter in texto:
    if caracter == " ":
        contador += 1

print(f"La cadena {texto}, contiene {contador} espcaios")