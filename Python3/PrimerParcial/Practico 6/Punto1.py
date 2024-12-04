from moduleFecha import Fecha 

#Clase SOCIO
class Socio:
    
    def __init__(self, nombre:str, nacimiento:'Fecha'):

        if not isinstance(nombre, str):
            raise ValueError("[!] El nombre no es un string")
        if not isinstance(nacimiento, Fecha):
            raise TypeError("[!] La fecha de nacimiento no es válida")
        
        self.__nombre = nombre
        self.__fechaNacimiento = nacimiento
        self.__fechaPenalizacion = None

    def __str__(self):
        return f"Nombre: {self.__nombre}, Fecha de nacimiento: {self.__fechaNacimiento}, Fecha de penalización: {self.__fechaPenalizacion}"
    

    # Los <<Comandos>>
    def establecerNombre(self, nombre:str):
        self.__nombre = nombre

    def establecerFechaNacimiento(self, fecha:'Fecha'):
        if not isinstance(fecha, Fecha):
            self.__fechaNacimiento = fecha

    def establecerFechaPenalizacion(self, hastaFecha:'Fecha'):
        if not isinstance(hastaFecha, Fecha):
            raise TypeError("[!] La fecha de penalización no es válida")
        self.__fechaPenalizacion = hastaFecha

    
    #Las <<Consultas>>
    def estaHabilitado(self, fecha:'Fecha') -> bool:
        """retorna True cuando no tiene fechaPenalizacion o cuando esta es anterior a la fecha recibida en el parametro"""
        if self.__fechaPenalizacion is None or self.__fechaPenalizacion.esAnterior(fecha):
            return True
        else:
            return False
        
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerFechaNacimiento(self) -> 'Fecha':
        return self.__fechaNacimiento
    
    def obtenerFechaPenalizacion(self) -> 'Fecha':
        return self.__fechaPenalizacion
    



# Clase LIBRO
class Libro:

    def __init__(self, nombre:str, autor:str, editorial:str, categoria:chr):
        if not isinstance(nombre, str) or nombre.isspace() or nombre == "":
            raise ValueError("[!] El nombre no es un string")
        if not isinstance(autor, str) or autor.isspace() or autor == "":
            raise ValueError("[!] El autor no es un string")
        if not isinstance(editorial, str) or editorial.isspace() or editorial == "":
            raise ValueError("[!] La editorial no es un string")
        if not categoria in ['A', 'B', 'C', 'D']:
            raise ValueError("[!] La categoria debe ser A, B, C o D")
        
        """
        isinstance(editorial, str): Verifica que el valor sea una cadena.
        editorial.isspace(): Detecta si la cadena solo contiene espacios en blanco.
        editorial == "": Asegura que la cadena no esté vacía.
        """

        self.__nombre = nombre
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria

    def __str__(self):
        return f"Nombre: {self.__nombre}, Autor: {self.__autor}, Editorial: {self.__editorial}, Categoria: {self.__categoria}"

    
    # Las <<Consultas>>

    def obtenerNombre(self) -> str:
        return self.__nombre

    def obtenerAutor(self) -> str:
        return self.__autor

    def obtenerEditorial(self) -> str:
        return self.__editorial

    def obtenerCategoria(self) -> chr:  
        return self.__categoria



# Clase PRESTAMO
class Prestamo():

    def __init__(self, libro:'Libro', fechaPrestamo:'Fecha', cantDias:int, socio:'Socio'):

        if not isinstance(libro, Libro):
            raise TypeError("[!] El libro no es válido")
        if not isinstance(fechaPrestamo, Fecha):
            raise TypeError("[!] La fecha de préstamo no es válida")
        if not isinstance(socio, Socio):
            raise TypeError("[!] El socio no es válido")
        if cantDias <= 0:
            raise ValueError("[!] La cantidad de días debe ser mayor a cero")

        if not socio.estaHabilitado(fechaPrestamo):
            raise ValueError("[!] El socio no está habilitado para realizar el préstamo")

        self.__libro = libro
        self.__fechaPrestamo = fechaPrestamo
        self.__fechaDevolucion = fechaPrestamo.sumaDias(cantDias)
        self.__socio = socio

    def __str__(self) -> str:
        return f"Prestamos del libro: {self.__libro.obtenerNombre()}, prestado a: {self.__socio.obtenerNombre()} desde {self.__fechaPrestamo}, hasta {self.__fechaDevolucion}"
        

    # Los <<Comandos>>
    def establecerFechaDevolucion(self, fechaDev:'Fecha'):
        if not isinstance(fechaDev, Fecha):
            raise TypeError("[!] La fecha de devolución no es válida")

        """establece la fecha de devolucion del libro y aplica penalizacion si es necesario"""
        if self.__fechaDevolucion.esAnterior(fechaDev):
            dias_diferencias = 0

            while self.__fechaDevolucion.esAnterior(fechaDev):
                self.__fechaDevolucion = self.__fechaDevolucion.diaSiguiente()
                dias_diferencias += 1

            if dias_diferencias < 7:
                dias_penalizacion = 3

            elif 7 <= dias_diferencias < 21:
                dias_penalizacion = 5
            
            elif dias_diferencias >= 21:
                dias_penalizacion = 10

            if self.__libro.obtenerCategoria() == 'A':
                dias_penalizacion *=2

            self.__socio.establecerFechaPenalizacion(fechaDev.sumaDias(dias_penalizacion))

        else:
            self.__fechaDevolucion = fechaDev

        
    #las <<Consultas>>
    def obtenerLibro(self) -> 'Libro':
        return self.__libro

    def obtenerFechaPrestamo(self) -> 'Fecha':
        return self.__fechaPrestamo

    def obtenerFechaDevolucion(self) -> 'Fecha':
        return self.__fechaDevolucion

    def estaAtrasado(self, fecha:'Fecha') -> bool:
        """retorna True cuando la fecha de devolución es posterior a la fecha recibida en el parametro"""
        if not isinstance(fecha, Fecha):
            raise TypeError("[!] La fecha no es válida")

        return self.__fechaDevolucion.esAnterior(fecha)

    def penalizacion(self) -> 'Fecha':
        """retorna la fecha de penalización del socio"""
        return self.__socio.obtenerFechaPenalizacion()


# La clase <<TESTER>>
class tester:
    @staticmethod
    def test():

        libro1 = Libro("El principito", "Antonio", "McEditors", 'A')
        libro2 = Libro("1984", "George Orwell", "Signet", 'B')
        print(libro1)
        print(libro2)


        socio1 = Socio("Juan Perez", Fecha(10,12,1985))
        socio2 = Socio("Maria Santiago", Fecha(25,6,1990))
        
        prestamo1 = Prestamo(libro1, Fecha(15,1,2021), 5, socio1)
        prestamo2 = Prestamo(libro2, Fecha(20,10,2021), 7, socio2)
        
        print(prestamo1)
        print(prestamo2)
        
        prestamo1.establecerFechaDevolucion(Fecha(25,1,2021))
        print(prestamo1)
        
        prestamo2.establecerFechaDevolucion(Fecha(27,10,2021))
        print(prestamo2)

        print(prestamo1.estaAtrasado(Fecha(24,1,2021)))
        print(prestamo2.estaAtrasado(Fecha(26,10,2021)))

        socio1.establecerFechaPenalizacion(Fecha(26,10,2021))

        print(socio1.penalizacion())
       


if __name__ == '__main__':
    tester.test()
                