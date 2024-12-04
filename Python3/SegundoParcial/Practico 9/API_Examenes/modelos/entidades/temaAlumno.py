#Importamos la clase Alumno para que reconozco el contrusctor
from modelos.entidades.alumno import Alumno
from modelos.entidades.tema import Tema

class TemaAlumno:

    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        return cls(Alumno.fromDiccionario(diccionario["alumno"]), Tema.fromDiccionario(diccionario["tema"]))

    def __init__(self, alumno:Alumno, tema:Tema):

        if not isinstance(alumno, Alumno):
            raise ValueError(f"El alumno debe ser una instancia de Alumno")
        
        if not isinstance(tema, Tema):
            raise ValueError(f"El tema debe ser una instancia de Tema")
        
        self.__alumno = alumno
        self.__tema = tema


    #<<consultas>>
    def obtenerAlumno(self) -> Alumno:
        return self.__alumno
    
    def obtenerTema(self) -> Tema:
        return self.__tema
    
    
    #<<comandos>>
    def establecerAlumno(self, alumno:Alumno):
        if not isinstance(alumno, Alumno):
            raise ValueError(f"El alumno debe ser una instancia de Alumno")
        self.__alumno = alumno

    def establecerTema(self, tema:Tema):
        if not isinstance(tema, Tema):
            raise ValueError(f"El tema debe ser una instancia de Tema")
        self.__tema = tema

    def toDiccionario(self) -> dict:
        return {
            "alumno":self.__alumno.toDiccionario(),
            "tema":self.__tema.toDiccionario()
        }
    
    

        
        