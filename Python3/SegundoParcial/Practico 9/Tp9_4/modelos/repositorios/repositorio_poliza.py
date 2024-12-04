from modelos.entidades.polizaInmueble import PolizaInmueble
from modelos.entidades.polizaInmuebleEscolar import PolizaInmuebleEscolar
import json


class RepositorioPoliza:
    __ruta_archivo = 'datos/polizas.json'

    def __init__(self):
        self.__polizas = self.__cargarTodos()

    def __cargarTodos(self):
        lista = []
        try:
            with open(self.__ruta_archivo, 'r') as archivo:
                datos = json.load(archivo)
                for poliza in datos:
                    if not "cantidadPersonas" in poliza:
                        lista.append(PolizaInmueble.fromDiccionario(poliza))
                    else:
                        lista.append(PolizaInmuebleEscolar.fromDiccionario(poliza))
        except FileNotFoundError:
            print("No se encontró el archivo de polizas")
        return lista
    
    def guardarTodos(self):
        try:
            with open(self.__ruta_archivo, 'w') as archivo:
                datos = [poliza.toDiccionario() for poliza in self.__polizas]
                json.dump(datos, archivo, indent=4)
        except FileNotFoundError:
            print("No se encontró el archivo de polizas")

    
    def obtenerTodos(self):
        return self.__polizas
    

    def existe(self, otraPoliza: PolizaInmueble):
        for poliza in self.__polizas:
            if poliza.obetenrNumero() == otraPoliza.obetenrNumero():
                return True
        return False
    
    def existeNumero(self, numero: int):
        for poliza in self.__polizas:
            if poliza.obetenrNumero() == numero:
                return True
        return False
    

    def agregarPoliza(self, Nuevapoliza: PolizaInmueble):
        if not self.existe(Nuevapoliza):
            self.__polizas.append(Nuevapoliza)
            self.guardarTodos()
            return True
        return False

    def eliminarPoliza(self, numero: int):
        for poliza in self.__polizas:
            if poliza.obetenrNumero() == numero:
                self.__polizas.remove(poliza)
                self.guardarTodos()
                return True
        return False
                

    def modificarPorNumero(self,numero:int,incendio:float,explosion:float,robo:float,cantPersonas:int=None,montoEquipamiento:float=None,montoInmobiliario:float=None,montoPersona:float=None):
        for poliza in self.__polizas:
            if poliza.obetenrNumero() == numero:
                poliza.establecerIncendio(incendio)
                poliza.establecerExplosion(explosion)
                poliza.establecerRobo(robo)

                if cantPersonas != None:
                    poliza.establecerCantPersonas(cantPersonas)
                    poliza.establecerMontoEquipamiento(montoEquipamiento)
                    poliza.establecerMontoInmobiliario(montoInmobiliario)
                    poliza.establecerMontoPersona(montoPersona)
                self.guardarTodos()
                return True
        return False