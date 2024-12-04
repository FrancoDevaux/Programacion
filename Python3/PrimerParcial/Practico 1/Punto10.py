"""
Escriba un programa que permita al usuario ingresar las medidas de 2 lados de un
rectángulo, y que luego mediante la impresión repetida de un caracter (ej: *) lo dibuje
en la pantalla. Para este ejercicio tomaremos un máximo de 40 para el lado más
largo, con el fin de evitar problemas de visualización en la consola. Verificar en los
datos de entrada que se cumpla este requisito.
"""

ancho= int(input("\nIngrese medida del primer lado: "))
alto = int(input("Ingrese medida del segundo lado: "))

while (alto > 40) or (ancho > 40):
    print("\n[!]Ingresa un numero menor a 40")
    alto= int(input("\nIngrese medida del primer lado: "))
    ancho = int(input("Ingrese medida del segundo lado: "))

#Dibujar el rectangulo
for i in range(alto):
    print("*" * ancho)