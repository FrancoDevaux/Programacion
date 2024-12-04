class Socio:

    #<<Metodos de clase>>
    @classmethod
    def fromDiccionario(cls, diccionario) -> 'Socio':
        if "dni" not in diccionario:
            raise ValueError("Falta el dni")
        if "nombre" not in diccionario:
            raise ValueError("Falta el nombre")
        if "apellido" not in diccionario:
            raise ValueError("Falta el apellido")
        if "mail" not in diccionario:
            raise ValueError("Falta el mail")
        if "fechaNacimiento" not in diccionario:
            raise ValueError("Falta la fecha de nacimiento")
        
        socio = cls(diccionario["dni"], diccionario["nombre"], diccionario["apellido"], diccionario["mail"], diccionario["fechaNacimiento"])
        return socio


    def __init__(self, dni:int, nombre:str, apellido:str, mail:str, fechaNacimiento:str):
        if not isinstance(dni, int) or dni < 0:
            raise ValueError("El dni debe ser de tipo int")
        
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser de tipo str")
        
        if not isinstance(apellido, str) or apellido == "" or apellido.isspace():
            raise ValueError("El apellido debe ser de tipo str")
        
        if not isinstance(mail, str) or mail == "" or mail.isspace():
            raise ValueError("El mail debe ser de tipo str")
        
        if not isinstance(fechaNacimiento, str) or fechaNacimiento == "" or fechaNacimiento.isspace():
            raise ValueError("La fecha de nacimiento debe ser de tipo str")
        
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__fechaNacimiento = fechaNacimiento

    def esIgual(self, otroSocio: 'Socio') -> bool:
        return self.__dni == otroSocio.obtenerDni()


    # <<Consultas>>
    def obtenerDni(self) -> int:
        return self.__dni
    
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerApellido(self) -> str:
        return self.__apellido
    
    def obtenerMail(self) -> str:
        return self.__mail
    
    def obtenerFechaNacimiento(self) -> str:
        return self.__fechaNacimiento
    

    # <<Comandos>>
    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser de tipo str")
        self.__nombre = nombre

    def establecerApellido(self, apellido:str):
        if not isinstance(apellido, str) or apellido == "" or apellido.isspace():
            raise ValueError("El apellido debe ser de tipo str")
        self.__apellido = apellido

    def establecerMail(self, mail:str):
        if not isinstance(mail, str) or mail == "" or mail.isspace():
            raise ValueError("El mail debe ser de tipo str")
        self.__mail = mail
    
    def establecerFechaNacimiento(self, fechaNacimiento:str):
        if not isinstance(fechaNacimiento, str) or fechaNacimiento == "" or fechaNacimiento.isspace():
            raise ValueError("La fecha de nacimiento debe ser de tipo str")
        self.__fechaNacimiento = fechaNacimiento
    
    def toDiccionario(self) -> dict:
        return {
            "dni": self.__dni,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "mail": self.__mail,
            "fechaNacimiento": self.__fechaNacimiento
        }