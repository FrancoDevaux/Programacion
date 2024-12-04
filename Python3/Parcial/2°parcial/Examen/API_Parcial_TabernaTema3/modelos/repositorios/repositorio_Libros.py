from modelos.entidades.libroDigital import LibroDigital
from modelos.entidades.libroFisico import LibroFisico
from modelos.entidades.libro import Libro
import json

class RepositorioLibros:
    __ruta_archivo = "datos/libros.json"

    def __init__(self):
        self.__libros = []
        self.__cargarLibros()

    def __cargarLibros(self):
        try:
            with open(RepositorioLibros.__ruta_archivo, 'r') as archivo:
                diccionario = json.load(archivo)
                for libro in diccionario:
                    if "formato" in libro:
                        self.__libros.append(LibroDigital.fromDiccionario(libro))
                    else:
                        self.__libros.append(LibroFisico.fromDiccionario(libro))
        except FileNotFoundError:
            print("No se encontró el archivo de libros")
        except Exception as e:
            print("Error cargando los libros del archivo.\n" + str(e))

    def __guardarLibros(self):
        try:
            with open(RepositorioLibros.__ruta_archivo, 'w') as archivo:
                lista_dicc = []
                for libro in self.__libros:
                    lista_dicc.append(libro.toDiccionario())
                json.dump(lista_dicc, archivo, indent=4)
        except Exception as e:
            print("Error guardando los libros en el archivo.\n" + str(e))

    def obtenerLibros(self):
        return self.__libros
    

    def obtenerLibroPorISBN(self, ISBN: int):
        if not isinstance(ISBN, int) or ISBN < 0:
            raise ValueError('El ISBN debe ser un entero positivo')
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                return libro
        return None
    
    def existeLibro(self, ISBN: int):
        if not isinstance(ISBN, int) or ISBN < 0:
            raise ValueError('El ISBN debe ser un entero positivo')
        #return self.obtenerLibroPorISBN(ISBN) != None #Corregi para que recorra uno por uno todos los libros de la lista y comparamos ISBN con el ISBN buscado Si encuentra una coincidencia, devuelve True, sino False.
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:  
                return True
        return False   
    

    def agregarLibro(self, libro: Libro):
        if not isinstance(libro, Libro):
            raise ValueError('El libro debe ser una instancia de Libro')
        
        if not self.existeLibro(libro.obtenerISBN()):
            self.__libros.append(libro)
            self.__guardarLibros()
            return True
        return False

        #if self.existeLibro(libro.obtenerISBN()):
           # raise ValueError('El libro ya existe')
        #self.__libros.append(libro)
        #self.__guardarLibros()
    

    def eliminarLibro(self, ISBN: int):
        if not isinstance(ISBN, int) or ISBN < 0:
            raise ValueError('El ISBN debe ser un entero positivo')
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                self.__libros.remove(libro)
                self.__guardarLibros()
                return True
        return False
    

    

    def modificarLibro(self, ISBN: int, libro_modificado: Libro):
        if not isinstance(ISBN, int) or ISBN < 0:
            raise ValueError('El ISBN debe ser un entero positivo')
        if not isinstance(libro_modificado, Libro):
            raise ValueError('El libro debe ser una instancia de Libro')
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                self.__libros.remove(libro)
                self.__libros.append(libro_modificado)
                self.__guardarLibros()
                return True
        return False
    

    
    
        
        
    



    
    