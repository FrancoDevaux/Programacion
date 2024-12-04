"""
Realizar un programa que solicite al usuario un número entero positivo, y luego en
pantalla muestre solamente los números pares desde el 1 hasta el número
ingresado.
Ej: usuario ingresa 10, en pantalla se mostrará 2 4 6 8 10
"""

numero = int(input("\nIngrese un numero: "))

while numero <= 0:
    print("[!]Numero no valido")
    numero = int(input("\nPorfavor ingrese otro numero: "))

for i in range(2, numero + 1, 2):
    print(i, end= " ")