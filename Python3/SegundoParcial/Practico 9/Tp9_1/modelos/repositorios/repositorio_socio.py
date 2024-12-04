from modelos.entidades.socio import Socio
import json

class RepositorioSocio:

    __ruta_archivo = "datos/socios.json"

    def __init__(self):
        self.__socios = self.__cargarTodos()

    def __cargarTodos(self):
        lista_socios = []
        try:
            with open(RepositorioSocio.__ruta_archivo, "r", encoding='utf-8') as archivo:
                socios = json.load(archivo)
                for socio in socios:
                    lista_socios.append(Socio.fromDiccionario(socio))                    
        except FileNotFoundError:
            print("No se encontro el archivo")
        return lista_socios
    
    def guardarTodos(self):
        try:
            with open(RepositorioSocio.__ruta_archivo, "w", encoding='utf-8') as archivo:
                socios = []
                for socio in self.__socios:
                    socios.append(socio.toDiccionario())
                json.dump(socios, archivo, indent=4)
        except FileNotFoundError:
            print("No se encontro el archivo")
  
    def obtenerTodos(self) -> list['Socio']:
        return self.__socios
    
    def existe(self, otroSocio:'Socio') -> bool:
        for socio in self.__socios:
            if socio.esIgual(otroSocio):
                return True
        return False
    
    def existeDni(self, dni:int) -> bool:
        for socio in self.__socios:
            if socio.obtenerDni() == dni:
                return True
        return False
    
    def agregar(self, nuevoSocio:'Socio'):
        if not isinstance(nuevoSocio, Socio):
            raise ValueError("El socio debe ser de tipo Socio")
        
        if self.existe(nuevoSocio):
            raise ValueError("El socio ya existe")
        self.__socios.append(nuevoSocio)
        self.guardarTodos()

    def modificarPorDni(self, dni:int, nombre:str, apellido:str, mail:str, fechaNacimiento:str) -> bool:
        for socio in self.__socios:
            if socio.obtenerDni() == dni:
                socio.establecerNombre(nombre)
                socio.establecerApellido(apellido)
                socio.establecerMail(mail)
                socio.establecerFechaNacimiento(fechaNacimiento)
                return True
        return False
    
    def eliminarPorDni(self, dni:int) -> bool:
        for socio in self.__socios:
            if socio.obtenerDni() == dni:
                self.__socios.remove(socio)
                self.guardarTodos()
                return True
        return False
    
    
    
