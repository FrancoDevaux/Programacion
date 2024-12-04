class Alumno:

    #<<atributo de clase>>
    __ultimoID = 0


    #<<Metodos de clase>>
    @classmethod
    def generarID(cls) -> int:
        cls.__ultimoID += 1
        return cls.__ultimoID
    
    @classmethod
    def obtenerUltimoID(cls) -> int:
        return cls.__ultimoID
    
    @classmethod
    def establecerUltimoID(cls, id: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError(f"El id debe ser un entero mayor a cero")
        cls.__ultimoID = id 
     
    @classmethod
    def fromDiccionario(cls, dicc:dict) -> "Alumno":

        if not isinstance(dicc, dict):
            raise ValueError(f"El diccionario debe ser un diccionario")
        
        if "id" in dicc:
            return cls(dicc["legajo"], dicc["apellido"], dicc["nombre"], dicc["id"])
        else:
            return cls(dicc["legajo"], dicc["apellido"], dicc["nombre"])



    #<<Metodos de instancia>>
    def __init__(self, legajo:int, apellido:str, nombre:str, id:int = None):

        if not isinstance(legajo, int) or legajo < 0:
            raise ValueError(f"El legajo debe ser un entero mayor a cero")
        
        if not isinstance(apellido, str) or apellido == "" or apellido.isspace():
            raise ValueError(f"El apellido debe ser una cadena no vacia")
        
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError(f"El nombre debe ser una cadena no vacia")
        
        if id != None:
            self.__id = id
        else:
            self.__id = Alumno.generarID()
        
        self.__legajo = legajo
        self.__apellido = apellido
        self.__nombre = nombre
        

    #<<consultas>>
    def obtenerID(self) -> int:
        return self.__id
    
    def obtenerLegajo(self) -> int:
        return self.__legajo    
    
    def obtenerApellido(self) -> str:
        return self.__apellido
    
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def toDiccionario(self) -> dict:
        return {"id": self.__id, "legajo": self.__legajo, "apellido": self.__apellido, "nombre": self.__nombre}
    
    
    #<<comandos>>
    def establecerLegajo(self, legajo:int):
        if not isinstance(legajo, int) or legajo < 0:
            raise ValueError(f"El legajo debe ser un entero mayor a cero")
        self.__legajo = legajo

    def establecerApellido(self, apellido:str):
        if not isinstance(apellido, str) or apellido == "" or apellido.isspace():
            raise ValueError(f"El apellido debe ser una cadena no vacia")
        self.__apellido = apellido

    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError(f"El nombre debe ser una cadena no vacia")
        self.__nombre = nombre

    
