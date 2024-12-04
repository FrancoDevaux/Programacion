from modelos.entidades.alumno import Alumno
import json

class RepositorioAlumno:

    __ruta_archivo = "datos/alumnos.json"

    def __init__(self):
        self.__alumnos = self.__cargarTodos()


    def __cargarTodos(self) -> list:
        lista_objetos = []
        try:
            lista_dicc = []
            with open(RepositorioAlumno.__ruta_archivo, "r", encoding="utf-8") as archivo:
                diccionarioDatos = json.load(archivo)
            lista_dicc = diccionarioDatos["alumnos"]
            Alumno.establecerUltimoID(diccionarioDatos["ultimoID"])

            for dicc in lista_dicc:
                lista_objetos.append(Alumno.fromDiccionario(dicc))
        except:
            print("No se pudo cargar el archivo alumnos.json")

        return lista_objetos

    def __guardarTodos(self):
        try:
            with open(RepositorioAlumno.__ruta_archivo, "w", encoding="utf-8") as archivo:
                lista_dicc = []
                for alumno in self.__alumnos:
                    lista_dicc.append(alumno.toDiccionario())
                diccionarioDatos = {
                    "ultimoID": Alumno.obtenerUltimoID(),
                    "alumnos": lista_dicc
                }
                json.dump(diccionarioDatos, archivo, indent=4)
        except:
            print("Error guardando el archivo alumnos.json")


    def obtenerTodos(self) -> list:
        return self.__alumnos
    
    def existeAlumnoConLegajo(self, legajo:int) -> bool:
        for alumno in self.__alumnos:
            if legajo == alumno.obtenerLegajo(): #Si el legajo ya existe
                return True
        return False     
    

    def agregar(self, alumno:Alumno):
        if not self.existeAlumnoConLegajo(alumno.obtenerLegajo()):
            self.__alumnos.append(alumno)
            self.__guardarTodos()
            return True
        else:
            return False
        

    def agregarDesdeDiccionario(self, dicc:dict):
        if not self.existeAlumnoConLegajo(dicc["legajo"]):
            alumno = Alumno.fromDiccionario(dicc)
            self.agregar(alumno)



    def obtenerPorLegajo(self, legajo:int) -> Alumno:
        for alumno in self.__alumnos:
            if alumno.obtenerLegajo() == legajo:
                return alumno
        return None


    def modificarLegajoPorDatosIndividuales(self, legajo:int, apellido:str, nombre:str):
        alum = self.obtenerPorLegajo(legajo)
        if alum is not None:
            alum.establecerApellido(apellido)
            alum.establecerNombre(nombre)
            self.__guardarTodos()
        else:
            raise ValueError("No existe un alumno con ese legajo")
    

    def modificarLegajoPorObjeto(self, alumno:Alumno):
        if self.existeAlumnoConLegajo(alumno.obtenerLegajo()):
            alumno_a_modificar = self.obtenerPorLegajo(alumno.obtenerLegajo())
            alumno_a_modificar.establecerApellido(alumno.obtenerApellido())
            alumno_a_modificar.establecerNombre(alumno.obtenerNombre())
            self.__guardarTodos()


    def eliminarPorLegajo(self, legajo:int) -> bool:
        for alumno in self.__alumnos:
            if alumno.obtenerLegajo() == legajo:
                self.__alumnos.remove(alumno)
                self.__guardarTodos()
                return True
        return False
    
    
        
             


