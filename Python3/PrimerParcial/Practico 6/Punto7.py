class Cuidador:
    
    def __init__(self, nombre:str, direccion:str, telefono:str):

        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__mascotas = []

    def __str__(self):
        return f"Cuidador: {self.__nombre}, Direccion: {self.__direccion}, Telefono: {self.__telefono}"
    
    def __repr__(self):
        return f"{self.__nombre}"
    

    # Los <<Comandos>>
    def establecerNombre(self, nombre:str):
        self.__nombre = nombre

    def establecerDireccion(self, direccion:str):
        self.__direccion = direccion

    def establecerTelefono(self, telefono:str):
        self.__telefono = telefono

    def agregarMascota(self, mascota:'Mascota'):
        if not isinstance(mascota, Mascota):
            raise ValueError("[!] La mascota no es un objeto Mascota")
        
        
        if mascota not in self.__mascotas:
            if mascota.obtenerCuidador() != None:
                mascota.obtenerCuidador().designarMascota(mascota)
            self.__mascotas.append(mascota)
            mascota.establecerCuidador(self)


    def designarMascota(self, mascota:'Mascota'):
        if not isinstance(mascota, Mascota):
            raise ValueError("[!] La mascota no es un objeto Mascota")
        
        if mascota in self.__mascotas:
            self.__mascotas.remove(mascota)
            #mascota.establecerCuidador(None)

    
    #Las <<Cosnultas>>
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerDireccion(self) -> str:
        return self.__direccion
    
    def obtenerTelefono(self) -> str:
        return self.__telefono
    
    def obtenerMascotas(self) -> list:
        return self.__mascotas


class Mascota:

    def __init__(self, nombre:str, especie:str, edad:int, descripcion:str):

        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
        self.__descripcion = descripcion
        self.__cuidador = None

    def __str__(self):
        mens=  f"Mascota: {self.__nombre}, Especie: {self.__especie}, Edad: {self.__edad}, Descripcion: {self.__descripcion}"

        if self.__cuidador == None:
            return f"{mens} Sin cuidador"
        
        return f"{mens}, Cuidador: {self.__cuidador.obtenerNombre()}"
    
    def __repr__(self):
        return f"({self.__nombre},{self.__especie})"
    

    # Los <<Comandos>>
    def establecerNombre(self, nombre:str):
        self.__nombre = nombre

    def establecerEspecie(self, especie:str):
        self.__especie = especie

    def establecerEdad(self, edad:int):
        self.__edad = edad

    def establecerDescripcion(self, descripcion:str):
        self.__descripcion = descripcion

    def establecerCuidador(self, cuidador:'Cuidador'):

        if not isinstance(cuidador, Cuidador):
            raise TypeError("[!] El cuidador no es válido")
        self.__cuidador = cuidador


    #Las <<Consultas>>

    def obtenerNombre(self) -> str:
        return self.__nombre

    def obtenerEspecie(self) -> str:
        return self.__especie

    def obtenerEdad(self) -> int:
        return self.__edad

    def obtenerDescripcion(self) -> str:
        return self.__descripcion

    def obtenerCuidador(self) -> 'Cuidador':
        return self.__cuidador


class Tester:
    @staticmethod
    def test():

        cuidador1 = Cuidador("Jorge", "Caracoles 123", "123456789")
        cuidador2 = Cuidador("Pepe", "Newbery 432", "1237894560")
        mascota1 = Mascota("Kitty", "Perro", 7, "Perro de raza")

        print(cuidador1)
        print(cuidador2)

        cuidador1.agregarMascota(mascota1)
        print(cuidador1.obtenerMascotas())
        print(mascota1)

        cuidador2.agregarMascota(mascota1)
        print(mascota1)
        print(cuidador1.obtenerMascotas())
        print(cuidador2.obtenerMascotas())
        print(mascota1)


if __name__ == "__main__":
    Tester.test()