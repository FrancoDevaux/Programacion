"""
Realizar un programa que solicite al usuario un número entero positivo, y luego en
pantalla muestre la secuencia de números desde el 1 hasta el número ingresado.
Ej: usuario ingresa 10, en pantalla se mostrará 1 2 3 4 5 6 7 8 9 10
"""

numero = int(input("\nIngrese un numero: "))

#Validar el numero

while numero <= 0:
    print("\n[!]El numero no es positivo")
    numero = int(input("\nIngrese un numero: "))

for i in range(1, numero + 1):
    print(i, end= " ")  #Si no pongo el end me va a imprimir uno bajo del otro
    