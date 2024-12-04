"""
Escriba un programa que permita el ingreso de números enteros positivos,
finalizando el ingreso con 0, y luego indique si la secuencia estaba ordenada de
menor a mayor.
"""

numero = int(input("\nIngrese numero (0 para finalizar): "))
lista_numeros = []

while numero != 0:
    lista_numeros.append(numero) #agregamos el ultimo numero que ingrese el usuario al final de la lista
    numero = int(input("Ingrese numero (0 para finalizar): "))

#Inicilaziar una bandera en true
ordenado = True 

#Verificar si la lista esta ordenada
for i in range(len(lista_numeros) - 1):
    if lista_numeros[i] > lista_numeros[i + 1]:
        ordenado = False
        break

#Imprimir por consola
if ordenado:
    print("\n[+]La secuencia esta ordenado de menor a mayor")
else:
    print("\n[!]La secuencia NO esta ordenada de menor a mayor.")
