#Una organización desea mantener información básica sobre sus empleados para
#calcular los sueldos, para ello diseñó la siguiente clase:

#A). implementar en python la clase Empleado.

#B). Escribir una clase tester para verificar los servicios de la clase Empleado
#utilizando el constructor con todos los parámetros. Esta verificación debe
#permitir al usuario ingresar los datos de un empleado (legajo, cantidad de
#horas trabajadas en el mes, y valor de la hora) y luego mostrar su legajo y el
#sueldo calculado 

#C). Escribir otra clase tester para verificar los servicios de la clase Empleado.
#Esta verificación debe permitir al usuario ingresar los datos de un empleado
#(legajo, cantidad de horas trabajadas en el mes, y valor de la hora), crear el
#objeto empleado utilizando el constructor con el parámetro legajo, y luego
#modificar los demás atributos del objeto con los servicios provistos por la
#clase. Finalmente debe mostrar por pantalla el legajo y el sueldo del
#empleado.


#Creamos la clase Emplado
class Empleado:

    #Ponemos los <<constructores>>
    def __init__(self, legajo:int, cantHoras:int=0, valorHora:float=0):
        """Resumen

        Argumentos:
            legajo (int): _descripcion
            cantHoras (int, opcional): _descripcion, Default a 0
            valorHora (int, opcional): _descripcion, Default a 0

        Raises:
            TypeError: _descripcion
            TypeError: _descripcion
            TypeError: _descripcion
        """

        #Declaramos los posibles errores 
        if legajo < 0:
            raise TypeError("\n[-]Valor del legajo incorrecto")
        if not isinstance(cantHoras,int) or cantHoras < 0:
            raise TypeError("\n[-]La cantidad de horas debe ser un numero entero mayor a cero")
        if not isinstance(valorHora,(int,float)) or valorHora < 0:
            raise TypeError("[-]Valor de hora incorrecto")
        

        self.__legajo = legajo
        self.__cantHoras = cantHoras
        self.__valorHora = valorHora



    #Creamos otra funcion que decia en <<comandos>>
    def establecerHorasTrabajadas(self, horas:int)->bool:

        """Resumen

            Argumentos:
                horas (int): _descripcion

            Retornos:
                bool: _descripcion
        """

        if not isinstance(horas,int):
            raise TypeError()
        
        if horas > -1:
            self.__cantHoras = horas
            return True
        else:
            return False
        

    #Creamos otra nueva funcion que decia en <<comandos>>
    def establecerValorHora(self,valor:float)->bool:
        """Resumen

            Argumentos:
                valor (float): _descripcion

            Retornos:
                bool: _descripcion
        """

        if valor > -1:
            self.__valorHora = valor
            return True
        else:
            return False


    #Creamos 4 funciones que estaban en <<consultas>>
    def obtenerLegajo(self)->int:
        return self.__legajo
    
    def obtenerHorasTrabajadas(self)->int:
        return self.__cantHoras
    
    def obtenerValorHora(self)->float:
        return self.__valorHora
    
    def obtenerSueldo(self)->float:
        return self.__cantHoras * self.__valorHora
    


#Creamos la clase Tester 
class TesterEmpleado:
    @staticmethod

    def test():
        empleado1 = Empleado(111,25,2000)
        empleado2= Empleado(222)

        print(f"\nSueldo del empleado1 {empleado1.obtenerSueldo()}$")
        print (f"Sueldo del empleado2 {empleado2.obtenerSueldo()}$")


        if empleado2.establecerHorasTrabajadas(30):
            print("\nEl empleado2 ahora trabajo 30 horas")
        else:
            print("Hubo un error para establecer la hora")

        if empleado2.establecerHorasTrabajadas(-5):
            print("El empleado2 ahora trabajo 30 horas")
        else:
            print("Hubo un error para establecer la hora")


        print(f"\nEl empleado2 trabajo {empleado2.obtenerHorasTrabajadas()} horas")
        print (f"El valor hora del empleado2 es: {empleado2.obtenerValorHora()}")
            
        if empleado2.establecerValorHora(3000):
            print(f"\nUna actualizacion empleado2 valor hora: {empleado2.obtenerValorHora()}")
        else:
            print("Hubo un error para establecer el valor de hora")

        if empleado2.establecerValorHora(-5000):
            print(f"\nUna actualizacion empleado2 valor hora {empleado2.obtenerValorHora()}")
        else:
            print("Hubo un error para establecer el valor de hora")

        print(f"\nSueldo del empleado2 ahora es de {empleado2.obtenerSueldo()}$")


if __name__ == "__main__":
    TesterEmpleado.test()




