#Una vinoteca tiene su depósito dividido en cuatro grandes secciones: Jugos sin
#alcohol, Vinos blancos, Vinos tintos jóvenes y Vinos tintos añejados. Cada sección
#del depósito puede almacenar un máximo de 5000 unidades de su respectivo
#producto. Al crearse la vinoteca, cada sección comienza con su capacidad máxima.
# La vinoteca puede vender productos de cualquiera de las cuatro secciones, lo que
#reduce la cantidad disponible en esa sección. Si la cantidad solicitada es mayor a la
#disponible en una sección, se vende lo que se pueda y se informa que no se pudo
#completar la venta. Además, es posible reponer la cantidad de un producto en una
#sección hasta alcanzar su capacidad máxima. Cada vinoteca puede modelarse con
#el siguiente diagrama:
#A). implementar en python la clase vinoteca
#B). implementar una clase tester que verifique los servicios de la clase Vinoteca con valores significativos.
#EXTRAS: cada ves que se repone un producto, se llena a su capacidad maxima
#EXTRAS: Si la cantidad en deposito no es suficiente, se vende lo que se puede


#Creamos la clase Vinoteca
class Vinoteca:
    #Atributo de clase
    CAPACIDAD_MAXIMA = 5000    #Este valor es constante para todas las instancias de la clase

    #Atributo de instancia
    def __init__(self, cantJugo:int=CAPACIDAD_MAXIMA, cantBlancos:int=CAPACIDAD_MAXIMA, cantTintosJovenes:int=CAPACIDAD_MAXIMA, cantTintosAnejados:int=CAPACIDAD_MAXIMA):

        self.__cantJugo = cantJugo
        self.__cantBlancos = cantBlancos
        self.__cantTintosJovenes = cantTintosJovenes
        self.__cantTintosAnejados = cantTintosAnejados


    #Creamos 8 funciones que estan en <<comandos>>

    #REPONER
    def reponerJugos(self):
        self.__cantJugo = Vinoteca.CAPACIDAD_MAXIMA

    def reponerVinosBlancos(self):
        self.__cantBlancos = Vinoteca.CAPACIDAD_MAXIMA

    def reponerVinosTintosJovenes(self):
        self.__cantTintosJovenes = Vinoteca.CAPACIDAD_MAXIMA

    def reponerVinosTintosAnejados(self):
        self.__cantTintosAnejados = Vinoteca.CAPACIDAD_MAXIMA


    #VENDER
    def venderJugos(self, x:int)->bool:
        if x > 0:
            if x > self.obtenerCantidadJugos():
                x = self.obtenerCantidadJugos() #Esto asegura que no se intente vender más vinos de los que realmente hay.
                print(f"\nSolo se vendieron {x}, porque exedio la cantidad ingresada a lo que hay")

            self.__cantJugo -= x
            return True  #Se actualiza la cantidad de vinos blancos en el inventario restando la cantidad vendida.
                         #El atributo __cantJugos (que es privado) almacena la cantidad total de vinos blancos.
        else:
            return False


    def venderVinosBlancos(self, x:int)->bool:
        if x > 0:
            if x > self.obtenerCantidadVinosBlancos():
                x = self.obtenerCantidadVinosBlancos() #Esto asegura que no se intente vender más vinos de los que realmente hay.
                print(f"\nSolo se vendieron {x}, porque exedio la cantidad ingresada a lo que hay")

            self.__cantJugo -= x
            return True  #Se actualiza la cantidad de vinos blancos en el inventario restando la cantidad vendida.
                         #El atributo __cantJugos (que es privado) almacena la cantidad total de vinos blancos.
        else:
            return False
        

    def venderVinosTintosJovenes(self, x:int)->bool:
        if x > 0:
            if x > self.obtenerCantidadVinosJovenes():
                x = self.obtenerCantidadVinosJovenes() #Esto asegura que no se intente vender más vinos de los que realmente hay.
                print(f"\nSolo se vendieron {x}, porque exedio la cantidad ingresada a lo que hay")

            self.__cantJugo -= x
            return True  #Se actualiza la cantidad de vinos blancos en el inventario restando la cantidad vendida.
                         #El atributo __cantJugos (que es privado) almacena la cantidad total de vinos blancos.
        else:
            return False


    def venderVinosTintosAnejados(self, x:int)->bool:
        if x > 0:
            if x > self.obtenerCantidadVinosAnejados():
                x = self.obtenerCantidadVinosAnejados() #Esto asegura que no se intente vender más vinos de los que realmente hay.
                print(f"\nSolo se vendieron {x}, porque exedio la cantidad ingresada a lo que hay")

            self.__cantJugo -= x
            return True  #Se actualiza la cantidad de vinos blancos en el inventario restando la cantidad vendida.
                         #El atributo __cantJugos (que es privado) almacena la cantidad total de vinos blancos.
        else:
            return False


    #Ponemos lo parametros en <<consultas>>
    def obtenerCantidadJugos(self)->int:
        return self.__cantJugo
    
    def obtenerCantidadVinosBlancos(self)->int:
        return self.__cantBlancos
    
    def obtenerCantidadVinosJovenes(self)->int:
        return self.__cantTintosJovenes
    
    def obtenerCantidadVinosAnejados(self)->int:
        return self.__cantTintosAnejados
    

#Creamos la clase Tester
class testerVinoteca:
    @staticmethod

    def test():
        Vinoteca1 = Vinoteca()
        print(Vinoteca1.obtenerCantidadJugos())

        if Vinoteca1.venderJugos(500):  #vendemos 500 jugos
            print(f"\nSe vendieron jugos, entonces ahora hay: {Vinoteca1.obtenerCantidadJugos()}")
        else:
            print("No se vendieorn jugos.")

        print(Vinoteca1.obtenerCantidadJugos())

        if Vinoteca1.venderJugos(7000):  #probamos con 70 y anda
            print(f"\nSe vendieron jugos, entonces ahora hay: {Vinoteca1.obtenerCantidadJugos()}")
        else:
            print("No se vendieorn jugos.")

        Vinoteca1.reponerJugos()
        print("\nSe reponen jugos")
        print(Vinoteca1.obtenerCantidadJugos())

if __name__ == "__main__":
    testerVinoteca.test()



"""Crea una nueva bodega (instancia de Vinoteca).
Comprueba la cantidad inicial de jugos.
Intenta vender 40 jugos.
Comprueba si la venta fue exitosa y muestra la nueva cantidad de jugos.
Intenta vender 6000 jugos (más de los disponibles).
Comprueba si la venta fue exitosa y muestra un mensaje de error.
Repone todos los jugos.
Comprueba que la cantidad de jugos sea la máxima permitida."""