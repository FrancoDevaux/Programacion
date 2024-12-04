class Tema:

    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        return cls(diccionario["numero"], diccionario["nombre"], diccionario["enunciado"])


    def __init__(self, numero:int, nombre:str, enunciado:str):
        if not isinstance(numero, int) or numero < 0:
            raise ValueError(f"El numero debe ser un entero mayor a cero")
        
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError(f"El nombre debe ser una cadena no vacia")
        
        if not isinstance(enunciado, str) or enunciado == "" or enunciado.isspace():
            raise ValueError(f"El enunciado debe ser una cadena no vacia")
        
        self.__numero = numero
        self.__nombre = nombre
        self.__enunciado = enunciado


    #<<consultas>>
    def obtenerNumero(self) -> int:
        return self.__numero
    
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerEnunciado(self) -> str:
        return self.__enunciado
   
    
    #<<comandos>>
    def establecerNumero(self, numero:int):
        if not isinstance(numero, int) or numero < 0:
            raise ValueError(f"El numero debe ser un entero mayor a cero")
        self.__numero = numero

    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError(f"El nombre debe ser una cadena no vacia")
        self.__nombre = nombre

    def establecerEnunciado(self, enunciado:str):
        if not isinstance(enunciado, str) or enunciado == "" or enunciado.isspace():
            raise ValueError(f"El enunciado debe ser una cadena no vacia")
        self.__enunciado = enunciado

    def toDiccionario(self) -> dict:
        return {
            "numero":self.__numero,
            "nombre":self.__nombre,
            "enunciado":self.__enunciado
        }

