"""
Se desea realizar una aplicación que solicite al usuario tres números enteros
positivos (A, B, y X), y que muestre por pantalla todos los múltiplos de X que estén
entre A y B inclusive
"""

A = int(input("\nIngrese el primer numero A: "))
B = int(input("Ingrese el segundo numero B: "))
X = int(input("Ingrese el tercer numero X: "))

#Validar que B sea > o = que A
while B < A:
    print("\n[!]B tiene que ser mayor o igual que A")
    B = int(input("Ingrese el segundo numero B: "))

#Encontrar los multiplos de X
print(f"\nLos multiplos de {X} entre {A} y {B} son: ")

for numero in range(A, B + 1):
    if numero % X == 0:
        print(numero, end= " ")