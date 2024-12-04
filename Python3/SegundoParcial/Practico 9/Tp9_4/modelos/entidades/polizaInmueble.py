class PolizaInmueble:

    @classmethod
    def fromDiccionario(cls, diccionario:dict) -> 'PolizaInmueble':
        return cls(diccionario['numero'], diccionario['incendio'], diccionario['explosion'], diccionario['robo'])


    def __init__(self, numero:int, incendio:float, explosion:float, robo:float):
        if not isinstance (numero, int):
            raise TypeError('El número de póliza debe ser un entero')
        
        if not isinstance (incendio, float):
            raise TypeError('El monto de incendio debe ser un número')
        
        if not isinstance (explosion, float):
            raise TypeError('El monto de explosión debe ser un número')
        
        if not isinstance (robo, float):
            raise TypeError('El monto de robo debe ser un número')
        
        self.__numero = numero
        self.__incendio = incendio
        self.__explosion = explosion
        self.__robo = robo


    #Calcula el valor mensual de la póliza de esta forma: 2% de la cobertura de inciendos + 1% de la cobertura de explosiones + 3% de la cobertura de robo
    def valorMensualPoliza(self) -> float:
        return self.__incendio * 0.02 + self.__explosion * 0.01 + self.__robo * 0.03


    #<<Comandos>>
    def obetenrNumero(self) -> int:
        return self.__numero
    
    def obtenerIncendio(self) -> float:
        return self.__incendio
    
    def obtenerExplosion(self) -> float:
        return self.__explosion
    
    def obtenerRobo(self) -> float:
        return self.__robo
    

    # <<Consultas>>
    def establecerNumero(self, numero:int) -> None:
        if not isinstance (numero, int):
            raise TypeError('El número de póliza debe ser un entero')
        self.__numero = numero

    def establecerIncendio(self, incendio:float) -> None:
        if not isinstance (incendio, float):
            raise TypeError('El monto de incendio debe ser un número')
        self.__incendio = incendio

    def establecerExplosion(self, explosion:float) -> None:
        if not isinstance (explosion, float):
            raise TypeError('El monto de explosión debe ser un número')
        self.__explosion = explosion

    def establecerRobo(self, robo:float) -> None:
        if not isinstance (robo, float):
            raise TypeError('El monto de robo debe ser un número')
        self.__robo = robo



    def toDiccionario(self) -> dict:
        return {
            'numero':self.__numero, 
            'incendio':self.__incendio, 
            'explosion':self.__explosion, 
            'robo':self.__robo
        }