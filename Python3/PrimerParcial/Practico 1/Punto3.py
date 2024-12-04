"""
Extienda el programa anterior para permitir múltiple cantidad de “manos” de pintura.
"""

ancho = float(input("\nIngerse ancho de la habitacion: "))
largo = float(input("\nIngerse largo de la habitacion: "))
alto = float(input("\nIngerse alto de la habitacion: "))
manos = int(input("Ingrese cantidad de manos a pasarle: "))

areaPintura = ((ancho*largo *2 + largo * alto *2 ) - 0.80 *2) * manos
unlitro = 10
litrosPintura = areaPintura / unlitro

print(f"\nSe va a necesitar {litrosPintura} litros de pintura")