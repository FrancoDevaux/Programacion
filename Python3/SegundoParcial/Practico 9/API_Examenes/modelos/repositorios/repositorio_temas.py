#Siempre vamos a querer agregar un objeto, buscar o pedirle todos los objetos, modificar un deteminado objeto y eliminar un objeto

from modelos.entidades.tema import Tema
import json

class RepositorioTema:
    __ruta_archivo = "datos/temas.json"

    def __init__(self):
        self.__temas = self.__cargarTodos()

    def __cargarTodos(self) -> list:
        lista_objetos = []
        try:
            lista_dicc = []
            with open(RepositorioTema.__ruta_archivo, "r", encoding="utf-8") as archivo:
                diccionarioDatos = json.load(archivo)
            lista_dicc = diccionarioDatos["temas"]
            Tema.establecerUltimoID(diccionarioDatos["ultimoID"])

            for dicc in lista_dicc:
                lista_objetos.append(Tema.fromDiccionario(dicc))
        except:
            print("No se pudo cargar el archivo temas.json")

        return lista_objetos
    

    def __guardarTodos(self):
        lista_dicc = []
        for objeto in self.__temas:
            lista_dicc.append(objeto.toDiccionario())
        
        try:
            with open(RepositorioTema.__ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(lista_dicc, archivo, indent=4)
        except:
            print("No se pudo guardar el archivo temas.json")

    
    def existeTemaNumero(self, numero:int) -> bool:
        if not isinstance(numero, int) or numero < 0:
            raise ValueError(f"El numero debe ser un entero mayor a cero")
        
        for tema in self.__temas:
            if numero == tema.obtenerNumero(): #Si el numero ya existe
                return True
        return False
    

    def agregar(self, tema_nuevo:Tema):
        if not self.existeTemaNumero(tema_nuevo.obtenerNumero()):
            self.__temas.append(tema_nuevo)
            self.__guardarTodos()
            


    def obtenerTodos(self) -> list:
        return self.__temas
    
    def obtenerTemaNumero(self, numero:int) -> Tema:
        if not isinstance(numero, int) or numero < 0:
            raise ValueError(f"El numero debe ser un entero mayor a cero")
        
        for tema in self.__temas:
            if numero == tema.obtenerNumero():
                return tema
        return None
    
    def eliminar(self, numero:int):
        if not isinstance(numero, int) or numero < 0:
            raise ValueError(f"El numero debe ser un entero mayor a cero")
        
        for tema in self.__temas:
            if numero == tema.obtenerNumero():
                self.__temas.remove(tema)
                self.__guardarTodos()
                return True
        return False
    

    def modificarPorNumero(self, numero:int, nombre:str, enunciado:str):
        if not isinstance(numero, int) or numero < 0:
            raise ValueError(f"El numero debe ser un entero mayor a cero")
        
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError(f"El nombre debe ser una cadena no vacia")
        
        if not isinstance(enunciado, str) or enunciado == "" or enunciado.isspace():
            raise ValueError(f"El enunciado debe ser una cadena no vacia")
        
        
        for tema in self.__temas:
            if numero == tema.obtenerNumero():
                tema.establecerNombre(nombre)
                tema.establecerEnunciado(enunciado)
                self.__guardarTodos()
                return True
        return False
    

    

