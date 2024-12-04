"""
Escriba un programa que permita el ingreso de números enteros positivos para
calcular su promedio, el ingreso finaliza cuando el usuario ingresa un número
negativo. Luego mostrar el promedio y la cantidad de valores que se ingresaron. Ej:
“El promedio es ….. con un total de …. ingresos.”
"""

numero = int(input("\nIngrese un numero: "))
contador = 0
suma = 0

while numero > 0:
    numero = int(input("\nIngrese un numero: "))

    if numero < 0:
        break

    suma += numero 
    contador += 1

if contador == 0:
    print("\n[!]Se ingreso numero no positivo")
else:
    promedio = suma / contador
    print(f"\nEl promedio es {promedio:.2f}% con un total de {contador} ingresos")