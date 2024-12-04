class Libro:
    
    #<<metodos de clase>>
    @classmethod
    def fromDiccionario(cls, diccionario) -> 'Libro':

        if "titulo" not in diccionario:
            raise ValueError("Falta el titulo")
        if "autor" not in diccionario:
            raise ValueError("Falta el autor")
        if "genero" not in diccionario:
            raise ValueError("Falta el genero")
        if "anio" not in diccionario:
            raise ValueError("Falta el anio")
        if "ISBN" not in diccionario:
            raise ValueError("Falta el ISBN")

        libro = cls(diccionario["titulo"], diccionario["autor"],diccionario["genero"], diccionario["anio"], diccionario["ISBN"])
        return libro
    

    #<<Constructor>>
    def __init__(self, titulo: str, autor: str, genero: str, anio: int, ISBN: str, cantidad_ejemplares:int= None):

        if not isinstance(titulo, str) or titulo == "" or titulo.isspace():
            raise ValueError("El titulo debe ser de tipo str")
        
        if not isinstance(autor, str) or autor == "" or autor.isspace():
            raise ValueError("El autor debe ser de tipo str")
        
        if not isinstance(genero, str) or genero == "" or genero.isspace():
            raise ValueError("El genero debe ser de tipo str")
        
        if not isinstance(anio, int) or anio < 0:
            raise ValueError("El anio debe ser de tipo int")
        
        if not isinstance(ISBN, str) or ISBN == "" or ISBN.isspace():
            raise ValueError("El ISBN debe ser de tipo str")


        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anio = anio
        self.__ISBN = ISBN
        self.__cantidad_ejemplares = cantidad_ejemplares

        


    
    def esIgual(self, otroLibro: 'Libro'):
        return self.__ISBN == otroLibro.obtenerISBN()

    # <<Consultas>>
    def obtenerTitulo(self) -> str:
        return self.__titulo
    
    def obtenerAutor(self) -> str:
        return self.__autor
    
    def obtenerGenero(self) -> str:
        return self.__genero
    
    def obtenerAnio(self) -> int:
        return self.__anio
    
    def obtenerISBN(self) -> str:
        return self.__ISBN
    

    # <<Comandos>>
    def establecerTitulo(self, titulo: str):
        if not isinstance(titulo, str) or titulo == "" or titulo.isspace():
            raise ValueError("El titulo debe ser de tipo str")
        self.__titulo = titulo

    def establecerAutor(self, autor: str):
        if not isinstance(autor, str) or autor == "" or autor.isspace():
            raise ValueError("El autor debe ser de tipo str")
        self.__autor = autor

    def establecerGenero(self, genero: str):
        if not isinstance(genero, str) or genero == "" or genero.isspace():
            raise ValueError("El genero debe ser de tipo str")
        self.__genero = genero

    def establecerAnio(self, anio: int):
        if not isinstance(anio, int) or anio < 0:
            raise ValueError("El anio debe ser de tipo int")
        self.__anio = anio

    def establecerISBN(self, ISBN: str):
        if not isinstance(ISBN, str) or ISBN == "" or ISBN.isspace():
            raise ValueError("El ISBN debe ser de tipo str")
        self.__ISBN = ISBN

    def toDiccionario(self):
        return {
            "titulo": self.__titulo,
            "autor": self.__autor,
            "genero": self.__genero,
            "anio": self.__anio,
            "ISBN": self.__ISBN
        }
    
