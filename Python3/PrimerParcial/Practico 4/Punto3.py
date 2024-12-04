#Se requiere un programa que modele el concepto de un Automóvil. Para simplificar
#consideraremos que un automóvil tiene solamente los siguientes atributos:
#Marca: el nombre del fabricante.
#Modelo: nombre del modelo.
#Año: año de fabricación.
#Velocidad máxima: velocidad máxima soportada por el vehículo en km/h.
#Velocidad actual: velocidad del vehículo en un momento dado en km/h.

#El siguiente diagrama modela el Automóvil:

#Es importante tener en cuenta que no se debe acelerar más allá de la velocidad máxima permitida para el automóvil. 
# De igual manera, tampoco es posibledesacelerar a una velocidad negativa. Si se cumplen estos casos, se debe
#establecer la velocidad en el límite correspondiente y mostrar por pantalla unmensaje.
#El tiempo estimado en horas se calcula como el cociente entre la distancia en kilómetros a recorrer y la velocidad 
# actual (en km/h), multiplicando este valor por 60 obtenemos la cantidad de minutos. 
# Considerar el caso especial cuando el auto se encuentre detenido, en este caso mostrar un 
# mensaje indicando que “el auto está detenido y no se puede calcular el tiempo para llegar”.

#A). implementar la clase en python
#B). implementar una clase tester que cree un objeto de clase Automovil, y que pida al usuario la cantidad de 
# iteraciones a realizar, luego para cada iteración deberá generar un número aleatorio 
# entre 0 y 3 que determinará la operación a realizar:

#● 0: acelerar(20)
#● 1: desacelerar(15)
#● 2: frenarPorCompleto()
#● 3: calcularMinutosParaLlegar(50)

#En cada iteracion se debe mostrar el valor que se modificará, la acción a realizar y el valor modificado 
#luego de la acción. Por ejemplo, 
#si tocó el valor 0 muestra: “velocidad = 100, acelerar, velocidad actual = 120”. En el caso del
#calculo del tiempo para llegar debe mostrar el tiempo para llegar.

#C). Realizar otra clase tester con la misma lógica, pero las operaciones a realizar
#deben recibir parámetros aleatorios (coherentes).

#-------------------------------------------------------------------------------------------------------------------------


import random  #porque tenemos que generar numero aleatorios

class Automovil:

    def __init__(self, marca:str, modelo:str, anio:int, velocidadMaxima:float, velocidadActual:float):

        if velocidadMaxima < 0 or velocidadActual < 0:
            raise TypeError("\n[-]La velocidad no puede ser negativa")
        if anio < 0:
            raise TypeError("El año no puede ser menor a cero")
        
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__velocidadMaxima = velocidadMaxima
        self.__velocidadActual = velocidadActual


    #Creamos los metodos que estaban en <<comandos>>
    def establecerMarca(self, marca:str)->bool:
        self.__marca = marca 

    def establecerModelok(self, modelo:str)->bool:
        self.__modelo = modelo

    def establecerAnio(self, anio:int)->bool:
        self.__anio = anio

    def establecerVelocidadMaxima(self, velocidadMaxima:float)->bool:
        self.__velocidadMaxima = velocidadMaxima

    def establecerVelocidadActual(self, velocidadActual:float)->bool:
        self.__velocidadActual = velocidadActual


    #los EXTRAS dentro <<comandos>>
    def acelerar(self, incrementoVel:int)->bool:

        if incrementoVel >= 0 and self.__velocidadActual < self.__velocidadMaxima:
            if (self.__velocidadActual + incrementoVel) >= self.__velocidadMaxima:
                self.__velocidadActual = self.__velocidadMaxima
            else:
                self.__velocidadActual += incrementoVel
            return True
        else:
            return False


    def desacelerar(self, decrementoVel:int)->bool:
        
        if decrementoVel >= 0 and (self.__velocidadActual - decrementoVel) >= 0:
            self.__velocidadActual -= decrementoVel
            return True
        else:
            return False
        

    def frenarPorCompleto(self)->bool:
        
        if self.__velocidadActual != 0:   #si la velocidad actual del vehículo es diferente de cero, que lo detenga.
            self.__velocidadActual = 0
            return True
        else:
            return False


    #Ahora ponemos la parte de <<consultas>>
    def obtenerMarca(self):
        return self.__marca
    
    def obtenerModelo(self):
        return self.__modelo
    
    def obtenerAnio(self):
        return self.__anio
    
    def obtenerVelocidadMaxima(self):
        return self.__velocidadMaxima

    def obtenerVelocidadActual(self):
        return self.__velocidadActual

    def calcularMinutosParaLlegar(self, distanciaKM:float)->int:

        if self.__velocidadActual > 0:
            minutos = distanciaKM / self.__velocidadActual * 60
            return minutos
        elif self.__velocidadActual == 0:
            return -1



#Creamos la clase Tester
class testerAutomovil():
    @staticmethod

    def test1():
        auto = Automovil("Nissan", "GTR", 2002, 200, 0)
        iteraciones = int(input("\nIngrese la cantidad de iteraciones a realizar: "))

        #Generar un numero random entre cero y tres
        for _ in range(iteraciones):

            n = random.randint(0,3)

            match n:  #MATCH es esencial para utilizar la estructura match-case en Python
                case 0: #acelerar(20)
                    print(f"\nVelocidad {auto.obtenerVelocidadActual()}Km/h" ,end="")
                    if auto.acelerar(20):
                        print(f" a {auto.obtenerVelocidadActual()} Km/h")
                    else:
                        print("[-]Limite de velocidad maxima alcanzda, lolamento")
                case 1:
                    print(f"\nVelocidad {auto.obtenerVelocidadActual()}Km/h" ,end="")
                    if auto.desacelerar(15):
                        print(f" a {auto.obtenerVelocidadActual()} Km/h")
                    else:
                        print("[-]No se pueder ir a 0 km menos")
                case 2:
                    print(f"\nVelocidad {auto.obtenerVelocidadActual()}Km/h" ,end="")
                    if auto.frenarPorCompleto():
                        print(f" a {auto.obtenerVelocidadActual()} Km/h")
                    else:
                        print("[-]El auto se encuntra detenido actualmente")
                case 3:
                    if auto.calcularMinutosParaLlegar(50) == -1: 
                        print("Auto esta detenido")
                    else:
                        print(f"El auto llega en {round(auto.calcularMinutosParaLlegar(50))} minutos")



    #Creamos el otro test pero con numeros full aleatorios para cada uno de los casos
    def test2():
        auto = Automovil("Nissan", "GTR", 2002, 200, 0)
        iteraciones = int(input("\nIngrese la cantidad de iteraciones a realizar: "))

        for _ in range(0,3):
            n = random.randint(0,3)

            match n:
                case 0:
                    print(f"\nVelocidad {auto.obtenerVelocidadActual()}Km/h" ,end="")
                    if auto.acelerar(random.randint(0,30)):
                        print(f" a {auto.obtenerVelocidadActual()} Km/h")
                    else:
                        print("[-]Limite de velocidad maxima alcanzda, lolamento")
                case 1:
                    print(f"\nVelocidad {auto.obtenerVelocidadActual()}Km/h" ,end="")
                    if auto.desacelerar(random.randint(0,30)):
                        print(f" a {auto.obtenerVelocidadActual()} Km/h")
                    else:
                        print("[-]No se pueder ir a 0 km menos")
                case 2:
                    print(f"\nVelocidad {auto.obtenerVelocidadActual()}Km/h" ,end="")
                    if auto.frenarPorCompleto():
                        print(f" a {auto.obtenerVelocidadActual()} Km/h")
                    else:
                        print("[-]El auto se encuntra detenido actualmente")
                case 3:
                    if auto.calcularMinutosParaLlegar(50) == -1: 
                        print("Auto esta detenido")
                    else:
                        km_a_recorrer = random.randint(0,1000)
                        print(f"El auto llega en {round(auto.calcularMinutosParaLlegar(50))} minutos, si se queire hacer {km_a_recorrer}KM")


if __name__ == "__main__":
    
    while True:
        try:
            opcion = input("\nIngrese que Test desea realizar si (1) o (2): ")
            if opcion == "1":
                testerAutomovil.test1()
                break
            elif opcion == "2":
                testerAutomovil.test2()
                break
        except ValueError:
            print("\n[!]Ingrese numero valdio")
        



























