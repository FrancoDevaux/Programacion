"""
Implemente un programa que a partir del ancho, alto y largo de una habitación
rectangular calcule cuántos litros de pintura se necesitan para pintarla. Suponiendo
que 1 litro de pintura sirve para 10m cuadrados y que la habitación tiene sólo una
puerta de 0,80 de ancho por 2 mts de alto
"""

ancho = float(input("\nIngerse ancho de la habitacion: "))
largo = float(input("\nIngerse largo de la habitacion: "))
alto = float(input("\nIngerse alto de la habitacion: "))

areaPintura = (ancho*largo *2 + largo * alto *2 ) - 0.80 *2
unlitro = 10
litrosPintura = areaPintura / unlitro

print(f"\nSe va a necesitar {litrosPintura} litros de pintura")