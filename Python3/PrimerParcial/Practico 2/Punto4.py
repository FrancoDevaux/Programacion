"""Escriba un programa que permita ingresar un número, se debe validar que
realmente se haya ingresado un número, y crear una lista para almacenar por
separado los dígitos del número. Luego recorrer la lista y mostrar el índice que
contiene el dígito mayor.
"""

def ingresarNumero():

    while True:
        try:
            numero = int(input("\nIngrese un numero: "))
            return numero
        except:
            print("[!]Error: Ingresa un numero y positivo porfavor")

def separar_digitos(numero):
    # digitos =  [int(d) for d in str(numero)]
    #Se puede tamb hacer de esta forma o la de abajo con el bucle for

    digitos = [] #Creamos una lista vacia para poner los numeros
    for digits in str(numero):   #Convertimos el numero en cadena para agregarlo a la lista
        digitos.append(int(digits))
    return digitos

def buscar_digitoMayor(digitos):
    digito_mayor = max(digitos)
    indice = digitos.index(digito_mayor)  #El index para encontrar la posicion de en este caso digito_mayor

    return digito_mayor, indice

def main():
    numero = ingresarNumero()
    digitos = separar_digitos(numero)
    digito_mayor, indice = buscar_digitoMayor(digitos)

    print(f"\n[+]El digito mayor es: {digito_mayor} y se encuentra en el indice: {indice}")

if __name__ == "__main__":
    main()
