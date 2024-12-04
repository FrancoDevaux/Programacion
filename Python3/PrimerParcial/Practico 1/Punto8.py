"""
Desarrollar un programa que permita al usuario indicar cuantos valores quiere
ingresar, luego que permita la carga de los valores por teclado y nos muestre
posteriormente la suma de los valores ingresados y su promedio.
"""

cantidad_valores = int(input("\nIngrese cantidad de valores a ingresar: "))
valores = [] 
#valores = [0] * cantidad_valores


for i in range(cantidad_valores):
    valor = float(input(f"\nIngrese el valor {i + 1}: "))
    valores.append(valor)
    #valores[i] = valor


suma = sum(valores)
promedio = suma / cantidad_valores

# Imprimimos los resultados
print("La suma de los valores es: ", suma)
print("El promedio de los valores es: ", promedio)