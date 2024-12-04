"""
Pedir 3 números enteros e implementar un algoritmo para determinar cuál es el
mayor de los 3 y mostrar un mensaje por pantalla 
"""

numero1 = int(input("\nIngrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))
numero3 = int(input("Ingrese tecer numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"El numero {numero1} es el mas grande")

elif numero2 > numero1 and numero2 > numero3:
    print(f"El numero {numero2} es el mas grande")

elif numero3 > numero1 and numero3 > numero2:
    print(f"El numero {numero3} es el mas grande")

elif numero1 == numero2 and numero2 == numero3:
    print("Los tres numeros son iguales")

else:
    print("[!]Eror...")