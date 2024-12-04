"""
Escriba una función llamada EsBisiesto que permita ingresar un número de año y
devuelva verdadero en caso que el año sea bisiesto, o falso cuando no lo es. Un año
es bisiesto si: es divisible entre cuatro y (no es divisible entre 100 o es divisible entre
400). Utilizarlo en un programa que permita ingresar dia, mes y año y muestre por
pantalla si la fecha es válida o no.
"""

def EsBisiesto(año):
    
    return (año % 4 == 0 and ( año % 100 != 0 or año % 400 == 0))


def ValidarFecha(dia, mes, año):
    if año <= 0:
        return False
    
    #Validar dia segun el mes y si es bisiesto
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if EsBisiesto(año):
        dias_mes[1] = 29

    if dia < 1 or dia > dias_mes[mes - 1]:
        return False
    
    return True



#Ingreso de datos
dia = int(input("\nIngrese el dia: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

if ValidarFecha(dia, mes, año):
    print("\n[+]La fecha es valida")

    if EsBisiesto(año):
        print(f"El año {año} es Bisiesto")
    else:
        print(f"El año {año} no es Bisiesto")
        
else:
    print("\n[-]La fecha no es valida")
