from modelos.entidades.alumno import Alumno
from modelos.entidades.tema import Tema
from modelos.entidades.temaAlumno import TemaAlumno
import json
import random
import os


class RepositorioTemaAlumno:
    __ruta_archivo = "datos/temaalumnos.json"

    def __init__(self):
        self.__temaalumnos = self.__cargarTodos()

    def __cargarTodos(self) -> list:
        try:
            lista_objetos = []
            lista_dicc = []
            with open(RepositorioTemaAlumno.__ruta_archivo, "r", encoding="utf-8") as archivo:
                lista_dicc = json.load(archivo)
        except:
            print("No se pudo cargar el archivo temaalumnos.json")
     
        if len(lista_dicc) > 0:
            for dicc in lista_dicc:
                lista_objetos.append(TemaAlumno.fromDiccionario(dicc))
        else:
            #combinacion aleatorio de alumnos y temas
            from modelos.repositorios.repositorios import obtenerRepoAlumnos, obtenerRepoTemas
            repo_alumnos = obtenerRepoAlumnos()
            repo_temas = obtenerRepoTemas()
            if len(repo_alumnos.obtenerTodos()) > 0 and len(repo_temas.obtenerTodos()) > 0:
                for alumno in repo_alumnos.obtenerTodos():
                    lista_objetos.append(TemaAlumno(alumno, random.choice(repo_temas.obtenerTodos())))
                self.guardarCombinacion(lista_objetos)
        return lista_objetos
    

    def guardarCombinacion(self, lista_objetos):
        lista_dicc = []
        for objeto in lista_objetos:
            lista_dicc.append(objeto.toDiccionario())
        with open(RepositorioTemaAlumno.__ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(lista_dicc, archivo, indent=4)



    def __guardarTodos(self):
        lista_dicc = []
        for objeto in self.__temaalumnos:
            lista_dicc.append(objeto.toDiccionario())
        
        try:
            with open(RepositorioTemaAlumno.__ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(lista_dicc, archivo, indent=4)
        except:
            print("No se pudo guardar el archivo temaalumnos.json")


    def obtenerPorAlumnoID(self, id:int) -> TemaAlumno:
        if not isinstance(id, int) or id < 0:
            raise ValueError(f"El id debe ser un entero mayor a cero")
        
        lista_objetos = []
        for objeto in self.__temaalumnos:
            if objeto.obtenerAlumno().obtenerID() == id:
                return objeto
        return None