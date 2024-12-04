from modelos.entidades.prestamo import Prestamo
from datetime import date
import json

class RepositorioPrestamo:

    __ruta_archivo = "datos/prestamos.json"

    def __init__(self):
        self.__prestamos = self.__cargarTodos()

    def __cargarTodos(self):
        lista_prestamos = []
        try:
            with open(RepositorioPrestamo.__ruta_archivo, "r", encoding='utf-8') as archivo:
                prestamos = json.load(archivo)
                for prestamo in prestamos:
                    lista_prestamos.append(Prestamo.fromDiccionario(prestamo))
        except FileNotFoundError:
            print("No se encontro el archivo")
        return lista_prestamos
    
    def guardarTodos(self):
        try:
            with open(RepositorioPrestamo.__ruta_archivo, "w", encoding='utf-8') as archivo:
                prestamos = []
                for prestamo in self.__prestamos:
                    prestamos.append(prestamo.toDiccionario())
                json.dump(prestamos, archivo, indent=4)
        except FileNotFoundError:
            print("No se encontro el archivo")

    def obtenerTodos(self) -> list['Prestamo']:
        return self.__prestamos
    

    #Devuelve True si existe un prestamo en la lista con la combinacion de valores recibidos por parametro
    def existe(self, socio_dni:int, libro_isbn:int, fecha_retiro:int) -> bool:
        
        if not isinstance(socio_dni, int) or not isinstance(libro_isbn, int) or not isinstance(fecha_retiro, int):
            raise ValueError("Los valores deben ser enteros")
        
        for prestamo in self.__prestamos:
            if prestamo.esIgual(socio_dni, libro_isbn, fecha_retiro):
                return True
        return False
    
    # Devulve el prestamo que coincida con los valores recibidos por paramentro, sino existe retorna None
    def obtenerPrestamo(self, socio_dni:int, libro_isbn:int, fecha_retiro:int) -> 'Prestamo':
        
        if not isinstance(socio_dni, int) or socio_dni < 0:
            raise ValueError("El dni debe ser un entero")
        
        if not isinstance(libro_isbn, int) or libro_isbn < 0:
            raise ValueError("El isbn debe ser un entero")
        
        if not isinstance(fecha_retiro, int) or fecha_retiro < 0:
            raise ValueError("La fecha de retiro debe ser un entero")
        
    
        for prestamo in self.__prestamos:
            if prestamo.esIgual(socio_dni, libro_isbn, fecha_retiro):
                return prestamo
        return None
    

    def agregar(self, nuevo_prestamo:Prestamo) -> bool:
        if not isinstance(nuevo_prestamo, Prestamo):
            raise ValueError("El prestamo debe ser un objeto de la clase Prestamo")
        
        if self.existe(nuevo_prestamo.obtenerSocioDni(), nuevo_prestamo.obtenerLibroIsbn(), nuevo_prestamo.obtenerFechaRetiro()):
            return False
        
        self.__prestamos.append(nuevo_prestamo)
        self.guardarTodos()
        return True


    def modificarPorID(self,id:int, socio_dni:int, libro_isbn:int, fecha_retiro:int, cant_dias:int, fecha_devolucion:int):
        for prestamo in self.__prestamos:
            if prestamo.obtenerId() == id:
                prestamo.establecerSocioDni(socio_dni)
                prestamo.establecerLibroIsbn(libro_isbn)
                prestamo.establecerFechaRetiro(fecha_retiro)
                prestamo.establecerCantDias(cant_dias)
                prestamo.establecerFechaDevolucion(fecha_devolucion)
                self.guardarTodos()
                return True
        return False
    

    def eliminarPorID(self, id:int) -> bool:
        for prestamo in self.__prestamos:
            if prestamo.obtenerId() == id:
                self.__prestamos.remove(prestamo)
                self.guardarTodos()
                return True
        return False
    

    #Entero retorna la cantidad de prestamos de libros que tienen ISBN recibido por paramentro y que aun no han sido devueltos
    def cantidadLibrosSinDevolver(self, isbn:int) -> int:
        if not isinstance(isbn, int) or isbn < 0:
            raise ValueError("El isbn debe ser un entero")
        
        cantidad = 0
        for prestamo in self.__prestamos:
            if prestamo.obtenerLibroIsbn() == isbn and prestamo.obtenerFechaDevolucion() == 0:
                cantidad += 1
        return cantidad

