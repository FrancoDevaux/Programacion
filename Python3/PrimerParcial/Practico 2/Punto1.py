"""
Escribir un procedimiento “reverso” que permita ingresar como parámetro una
cadena, y devuelva la cadena invertida (“hola” se convierte en “aloh”). Escribir luego
un programa que determine si una cadena de caracteres es un palíndromo (un
palíndromo es un texto que se lee igual en sentido directo y en inverso, ej.: “radar”).
Sugerencia: para evitar diferencias entre mayúsculas y minúsculas en las cadenas,
utilice la función del tipo string .upper() ó .lower() en las cadenas, ya que Radar es
distinto a radaR.
"""


def reverso(cadena):

    return cadena[::-1]  #Forma de poner la cadena invertida

def es_palindromo(cadena):
    
    cadena = cadena.lower()  #Convertir la cadena a minuscula para ignorar mayusculas 
    cadena = cadena.replace(" ", "")  #Elimina los espacios en blanco 
    
    return cadena == reverso(cadena) #Compara la cadena original con su versión invertida. 
                                    #Si ambas son iguales, significa que la cadena se lee igual 
                                    # de izquierda a derecha que de derecha a izquierda, y por lo tanto, 
                                    # es un palíndromo.


#Pedir al usuario que ingrese una palabra
palabra = input("\nIngrese una palabra: ")

if es_palindromo(palabra):
    print(f"[+]La palabra {palabra} es palindromo")

else:
    print(f"[-]La palbra {palabra} no es polindormo")