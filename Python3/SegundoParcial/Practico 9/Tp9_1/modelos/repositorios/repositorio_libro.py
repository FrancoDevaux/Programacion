from modelos.entidades.libro import Libro
import json

class RepositorioLibro:
    __ruta_archivo = "datos/libros.json"

    def __init__(self):
        self.__libros = self.__cargarTodos()

    def __cargarTodos(self):
        lista_libros = []
        try:
            with open(RepositorioLibro.__ruta_archivo, "r", encoding='utf-8') as archivo:
                libros = json.load(archivo)
                for libro in libros:
                    lista_libros.append(Libro.fromDiccionario(libro))                    
        except FileNotFoundError:
            print("No se encontro el archivo")
        return lista_libros
    
    def guardarTodos(self):
        try:
            with open(RepositorioLibro.__ruta_archivo, "w", encoding='utf-8') as archivo:
                libros = []
                for libro in self.__libros:
                    libros.append(libro.toDiccionario())
                json.dump(libros, archivo, indent=4)
        except FileNotFoundError:
            print("No se encontro el archivo")

    
    def obtenerTodos(self) -> list['Libro']:
        return self.__libros
    
    def existe(self, otroLibro:'Libro') -> bool:
        for libro in self.__libros:
            if libro.esIgual(otroLibro):
                return True
        return False
    
    def existeISBN(self, ISBN:str) -> bool:
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                return True
        return False
    
    def agregar(self, nuevoLibro:'Libro'):
        if not isinstance(nuevoLibro, Libro):
            raise ValueError("El libro debe ser de tipo Libro")
        
        if self.existe(nuevoLibro):
            raise ValueError("El libro ya existe")
        self.__libros.append(nuevoLibro)
        self.guardarTodos()

    def modificarPorISBN(self, ISBN:str, titulo:str, autor:str, anio:int, genero:str) -> bool:
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                libro.establecerTitulo(titulo)
                libro.establecerAutor(autor)
                libro.establecerAnio(anio)
                libro.establecerGenero(genero)
                self.guardarTodos()
                return True
        return False
    

    def eliminarPorISBN(self, ISBN:str) -> bool:
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                self.__libros.remove(libro)
                self.guardarTodos()
                return True
        return False
        