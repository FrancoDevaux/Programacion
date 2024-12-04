from modelos.entidades.polizaInmueble import PolizaInmueble

class PolizaInmuebleEscolar(PolizaInmueble):

    @classmethod
    def fromDiccionario(cls, diccionario:dict) -> 'PolizaInmuebleEscolar':
        return cls(diccionario['numero'], diccionario['incendio'], diccionario['explosion'], diccionario['robo'], diccionario['cantPersonas'], diccionario['montoEquipamiento'], diccionario['montoInmobiliario'], diccionario['montoPersona'])



    def __init__(self,numero: int, incendio: float, explosion: float, robo:float,cantPersonas: int, montoEquipamiento: float, montoInmobiliario: float, montoPersona: float):
        super().__init__(numero, incendio, explosion, robo)
        self.__cantPersonas = cantPersonas
        self.__montoEquipamiento = montoEquipamiento
        self.__montoInmobiliario = montoInmobiliario
        self.__montoPersona = montoPersona



    #1% de la cobertura de incendios + 1% de la cobertura de explosiones + 2% de la cobertura de robo + 1% del monto de equipamiento + 1% del monto inmobiliario + 1% del monto por persona
    def valorMensualPoliza(self) -> float:
        return super().obtenerIncendio()*0.01 + super().obtenerExplosion()*0.01 + super().obtenerRobo()*0.02 + self.__montoEquipamiento*0.01 + self.__montoInmobiliario*0.01 +(self.__montoPersona*self.__cantPersonas)*0.01
        

    #<<Consultas>>
    def cantidadPersonas(self) -> int:
        return self.__cantPersonas
    
    def montoEquipamiento(self) -> float:
        return self.__montoEquipamiento
    
    def montoInmobiliario(self) -> float:
        return self.__montoInmobiliario
    
    def montoPersona(self) -> float:
        return self.__montoPersona
    


    # <<Comandos>>
    def establecerCantPersonas(self, cantPersonas:int) -> None:
        if not isinstance (cantPersonas, int):
            raise TypeError('La cantidad de personas debe ser un entero')
        self.__cantPersonas = cantPersonas

    def establecerMontoEquipamiento(self, montoEquipamiento:float) -> None:
        if not isinstance (montoEquipamiento, float):
            raise TypeError('El monto de equipamiento debe ser un número')
        self.__montoEquipamiento = montoEquipamiento

    def establecerMontoInmobiliario(self, montoInmobiliario:float) -> None:
        if not isinstance (montoInmobiliario, float):
            raise TypeError('El monto inmobiliario debe ser un número')
        self.__montoInmobiliario = montoInmobiliario

    def establecerMontoPersona(self, montoPersona:float) -> None:
        if not isinstance (montoPersona, float):
            raise TypeError('El monto por persona debe ser un número')
        self.__montoPersona = montoPersona

    
    def toDiccionario(self) -> dict:
        return {
            'numero': self.obetenrNumero(),
            'incendio': self.obtenerIncendio(),
            'explosion': self.obtenerExplosion(),
            'robo': self.obtenerRobo(),
            'cantPersonas': self.__cantPersonas,
            'montoEquipamiento': self.__montoEquipamiento,
            'montoInmobiliario': self.__montoInmobiliario,
            'montoPersona': self.__montoPersona
        }
        