from datetime import date
import json

class Prestamo:

    # <<Atributos de clase>>
    __uiltimoID = 0
    __ruta_archivo = "datos/prestamos.json"

    # <<Metodos de clase>>
    @classmethod
    def fromDiccionario(cls, diccionario) -> 'Prestamo':
        if "id" not in diccionario:
            raise ValueError("Falta el id")
        if "socio_dni" not in diccionario:
            raise ValueError("Falta el dni del socio")
        if "libro_isbn" not in diccionario:
            raise ValueError("Falta el isbn del libro")
        if "fecha_retiro" not in diccionario:
            raise ValueError("Falta la fecha de retiro")
        if "cant_dias" not in diccionario:
            raise ValueError("Falta la cantidad de dias")
        if "fecha_devolucion" not in diccionario:
            raise ValueError("Falta la fecha de devolucion")
        
        prestamo = cls(diccionario["id"], diccionario["socio_dni"], diccionario["libro_isbn"], diccionario["fecha_retiro"], diccionario["cant_dias"], diccionario["fecha_devolucion"])
        return prestamo
    
    #Se utiliza pra obtener in ID unico para cada nueva instancia, incrementa el atributo de clase ultimoID y lo retorna
    @classmethod
    def obtenerNuevoID(cls) -> int:
        Prestamo.ultimoID += 1
        return Prestamo.ultimoID
    
    #Se utiliza cuando inicia el sistema y establece el ultimo id utilizado a 0 si no se encuentra el archivo datos
    @classmethod
    def establecerUltimoID(cls, id:int):
        try:
            with open(Prestamo.__ruta_archivo, "r") as archivo:
                datos = json.load(archivo)
                if len(datos) > 0:
                    Prestamo.ultimoID = datos[-1]["id"]
                else:
                    Prestamo.ultimoID = 0
        except FileNotFoundError:
            Prestamo.ultimoID = 0




    # <<Constructor>>
    def __init__(self, id:int, socio_dni:int, libro_isbn:int, fecha_retiro:date, cant_dias:int, fecha_devolucion:date = None):

        if not isinstance(id, int) or id < 0:
            raise ValueError("El id debe ser de tipo int")
        
        if not isinstance(socio_dni, int) or socio_dni < 0:
            raise ValueError("El dni del socio debe ser de tipo int")
        
        if not isinstance(libro_isbn, int) or libro_isbn < 0:
            raise ValueError("El isbn del libro debe ser de tipo int")
        
        if not isinstance(fecha_retiro, date):
            raise ValueError("La fecha de retiro debe ser de tipo date")
        
        if not isinstance(cant_dias, int) or cant_dias < 0:
            raise ValueError("La cantidad de dias debe ser de tipo int")
        
        if not isinstance(fecha_devolucion, date):
            raise ValueError("La fecha de devolucion debe ser de tipo date")
        
        self.__id = id
        self.__socio_dni = socio_dni
        self.__libro_isbn = libro_isbn
        self.__fecha_retiro = fecha_retiro
        self.__cant_dias = cant_dias
        self.__fecha_devolucion = fecha_devolucion


    def esIgual(self, otroPrestamo: 'Prestamo') -> bool:
        return self.__id == otroPrestamo.obtenerSocioDni() and self.__libro_isbn == otroPrestamo.obtenerLibroIsbn() and self.__fecha_retiro == otroPrestamo.obtenerFechaRetiro() and self.__cant_dias == otroPrestamo.obtenerCantDias() and self.__fecha_devolucion == otroPrestamo.obtenerFechaDevolucion()  
    
    # <<Consultas>>
    def obtenerId(self) -> int:
        return self.__id
    
    def obtenerSocioDni(self) -> int:
        return self.__socio_dni
    
    def obtenerLibroIsbn(self) -> int:
        return self.__libro_isbn
    
    def obtenerFechaRetiro(self) -> str:
        return self.__fecha_retiro
    
    def obtenerCantDias(self) -> int:
        return self.__cant_dias
    
    def obtenerFechaDevolucion(self) -> str:
        return self.__fecha_devolucion
    

    # <<Comandos>>
    def establecerSocioDni(self, socio_dni:int):
        if not isinstance(socio_dni, int) or socio_dni < 0:
            raise ValueError("El dni del socio debe ser de tipo int")
        self.__socio_dni = socio_dni

    def establecerLibroIsbn(self, libro_isbn:int):
        if not isinstance(libro_isbn, int) or libro_isbn < 0:
            raise ValueError("El isbn del libro debe ser de tipo int")
        self.__libro_isbn = libro_isbn

    def establecerFechaRetiro(self, fecha_retiro:str):
        if not isinstance(fecha_retiro, str) or fecha_retiro == "" or fecha_retiro.isspace():
            raise ValueError("La fecha de retiro debe ser de tipo str")
        self.__fecha_retiro = fecha_retiro

    def establecerCantDias(self, cant_dias:int):
        if not isinstance(cant_dias, int) or cant_dias < 0:
            raise ValueError("La cantidad de dias debe ser de tipo int")
        self.__cant_dias = cant_dias

    def establecerFechaDevolucion(self, fecha_devolucion:str):
        if not isinstance(fecha_devolucion, str) or fecha_devolucion == "" or fecha_devolucion.isspace():
            raise ValueError("La fecha de devolucion debe ser de tipo str")
        self.__fecha_devolucion = fecha_devolucion

    
    def toDiccionario(self) -> dict:
        return {
            "id": self.__id,
            "socio_dni": self.__socio_dni,
            "libro_isbn": self.__libro_isbn,
            "fecha_retiro": self.__fecha_retiro,
            "cant_dias": self.__cant_dias,
            "fecha_devolucion": self.__fecha_devolucion
        }