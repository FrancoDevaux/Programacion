from abc import ABC, abstractmethod

class Color:
    pass

class Prenda(ABC):

    def __init__(self, codigo: int, nombre: str, precio:float, talle: float, color:'Color', stock:int):

        if not isinstance(codigo, int) or codigo < 0:
            raise ValueError("El código debe ser un número entero positivo.")
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre de la prenda no puede estar vacío.")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("Error: El precio debe ser un número positivo.")
        if not isinstance(talle, float) or talle <= 0:
            raise ValueError("El talle debe ser un número positivo.")
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("El stock debe ser un número entero positivo.")
        

        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._talle = talle
        self._color = color
        self._stock = stock


    @abstractmethod
    def obtenerDescripcion(self) -> str:
        pass

    def obtenerCosto(self) -> float:
        return self._precio * self._stock   #Calculamos el valor total
    
    def stockDisponible(self, cantidad:int) -> bool:
        return self._stock >= cantidad   #Ver si hay suficiente stock
        
    
class Ropa(Prenda):

    def __init__(self, codigo: int, nombre: str, precio:float, talle: float, color:'Color', stock:int, estacional: bool, planchado: bool, aptoLavarropas: bool):
        super().__init__(codigo, nombre, precio, talle, color, stock)

        if not isinstance(estacional, bool):
            raise ValueError("La estacionalidad debe ser un booleano.")
        
        if not isinstance(planchado, bool):
            raise ValueError("El planchado debe ser un booleano.")
        
        if not isinstance(aptoLavarropas, bool):
            raise ValueError("El estado de aptitud para lavarropas debe ser un booleano.")


        self.__estacional = estacional
        self.__planchado = planchado
        self.__aptoLavarropas = aptoLavarropas


    def obtenerDescripcion(self) -> str:
        return f"{self._nombre} , Talle: {self._talle} , Precio: {self._precio} , Stock: {self._stock} , Estacional: {self.__estacional}   "
    
    def esEstacional(self) -> bool:
        return self.__estacional

    def requierePlanchado(self) -> bool:
        return self.__planchado

    def esAptoLavarropas(self) -> bool:
        return self.__aptoLavarropas
    

class Calzado(Prenda):

    def __init__(self, codigo: int, nombre: str, precio:float, talle: float, color:'Color', stock:int, material: str, suela: str, deportivo: bool):
        super().__init__(codigo, nombre, precio, talle, color, stock)

        if not isinstance(material, str) or material == "" or material.isspace():
            raise ValueError("Error: El material del calzado no puede estar vacío.")
        
        if not isinstance(suela, str) or suela == "" or suela.isspace():
            raise ValueError("La suela del calzado no puede estar vacía.")
        
        if not isinstance(deportivo, bool):
            raise ValueError("El estado de deportivo debe ser un booleano.")

        self.__material = material
        self.__suela = suela
        self.__deportivo = deportivo


    def obtenerDescripcion(self) -> str:
        return f"{self._nombre} , Material: {self.__material}, Suela: {self.__suela}, Deportivo: {self.__deportivo})"

    def esDeportivo(self):
        return self.__deportivo