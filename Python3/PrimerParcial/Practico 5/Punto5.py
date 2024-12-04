class Especie:

    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__machos = 0
        self.__hembras = 0
        self.__ritmos = 0.0

    
    # Las <<Consultas Triviales>>
    def obtenerMachos(self):
        return self.__machos
    
    def obtenerHembras(self):
        return self.__hembras
    
    def obtenerRitmo(self):
        return self.__ritmos
    

    # Las <<Consultas>>
    def poblacionAbual(self) -> int:
        return self.__machos + self.__hembras
    
    def poblacionEstimada(self, anios:int) -> int:
        return int(self.__ritmos * anios)
    
    def anioParaPoblacion(self, poblacion:int) -> int:
        if self.__ritmos > 0:
            return poblacion / self.__ritmos
        else:
            return 0
        
    def riesgo(self) -> str:
        if self.__ritmos < 0.5:
            return "Bajo"
        elif self.__ritmos < 1.0:
            return "Medio"
        else:
            return "Alto"
        
    def masHembras(self) -> bool:
        pass
    
    def mayorRitmo(self, otraEspecie:"Especie") -> "Especie":
        """devuelve la referencia al objeto con mayor ritmo de crecimiento"""
        if self.__ritmos > otraEspecie.obtenerRitmo():
            return self
        elif self.__ritmos < otraEspecie:
            return otraEspecie 
        else:
            print("Tienen el mismo ritmo de crecimiento")

    def clonar(self) -> "Especie":
        """devuelve un nuevo objeto Especie con el mismo esatdo interno el objeto que recibe el mensaje"""
        pass
        #return eval(self.__repr__())

    def toString(self) -> str:
        return f"Especie: {self.__nombre}, Machos: {self.__machos}, Hembras: {self.__hembras}, Ritmo: {self.__ritmos}"
    

    #Los <<Comandos>>
    def establecerHembras(self, cantHembras:int):
        if cantHembras >= 0:
            self.__hembras = cantHembras

    def establecerMachos(self, cantMachos:int):
        if cantMachos >= 0:
            self.__machos = cantMachos

    def establecerRitmo(self, ritmo:float):
        if ritmo >= 0.0:
            self.__ritmos = ritmo

    def actualizarHembras(self, cantHembras:int):
        if self.__hembras + cantHembras >= 0:
            self.__hembras += cantHembras
        else:
            print("No se puede actualizar la cantidad de hembras")

    def actualizarMachos(self, cantMachos:int):
        if self.__machos + cantMachos >= 0:
            self.__machos += cantMachos
        else:
            print("No se puede actualizar la cantidad de machos")

    def actualizarRitmo(self, ritmo:float):
        if ritmo >= 0.0:
            self.__ritmos = ritmo
        else:
            print("No se puede actualizar el ritmo de crecimiento")


# Ahora la clase <<Tester>>
class Tester:
    @staticmethod
    def test():
        especie1 = Especie("Perro")
        especie2 = Especie("Gato")
        
        print(especie1.toString())
        print(especie2.toString())
        
        especie1.establecerHembras(5)
        especie1.establecerMachos(10)
        especie1.establecerRitmo(0.8)
        
        print(especie1.toString())
        
        especie2.establecerHembras(15)
        especie2.establecerMachos(20)
        especie2.establecerRitmo(1.2)
        
        print(especie2.toString())
        
        especie1.actualizarHembras(3)
        especie1.actualizarMachos(2)
        especie1.actualizarRitmo(0.9)
        
        print(especie1.toString())

if __name__ == '__main__':
    Tester.test()