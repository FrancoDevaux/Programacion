"""
Realizar un programa que pida los tres lados de un triángulo e indique el tipo de
triángulo que es según sus lados: Equilátero (tres lados iguales), Isósceles (dos
lados iguales) o Escaleno (tres lados distintos).
"""

lado1 = float(input("\nIngrese primer lado: "))
lado2 = float(input("Ingrese segudno lado: "))
lado3= float(input("Ingrese tercer lado: "))


if lado1 == lado2 and lado2 == lado3:
    
    print("\nEl triangulo es Equilatero")

elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:

    print("\nEl trienagulo es Isoceles")

elif lado1 != lado2 or lado2 != lado3 or lado3!= lado1:
    print("\nEl triangulo es Escaleo")

else:
    print("\nNumeros invalidos")