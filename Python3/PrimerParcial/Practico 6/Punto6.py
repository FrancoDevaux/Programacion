class Participante:

    def __init__(self, nombre:str, edad:int, nacionalidad:str):

        if not isinstance(nombre, str):
            raise ValueError("[!] El nombre no es un string")
        if not isinstance(edad, int) or edad <= 0:
            raise ValueError("[!] La edad no es un número positivo")
        if not isinstance(nacionalidad, str):
            raise ValueError("[!] La nacionalidad no es un string")
        
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__disciplina = []

    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Nacionalidad: {self.__nacionalidad}"
    
    def __repr__(self):
        return f"({self.__nombre})"
    

    #Los <<Comandos>>
    def establecerNombre(self, nombre:str):
        self.__nombre = nombre

    def establecerEdad(self, edad:int): 
        self.__edad = edad

    def establecerNacionalidad(self, nacionalidad:str):
        self.__nacionalidad = nacionalidad

    def agregarDisciplina(self, disciplina:'Disciplina'):
        if not isinstance(disciplina, Disciplina):
            raise ValueError("[!] La disciplina no es un string")
        
        if disciplina not in self.__disciplina:
            self.__disciplina.append(disciplina)


    #Las <<Consultas>>
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerEdad(self) -> int:
        return self.__edad
    
    def obtenerNacionalidad(self) -> str:
        return self.__nacionalidad
    
    def obtenerDisciplinas(self) -> list:
        return self.__disciplina
    


# Clase DISCIPLINAS
class Disciplina:

    def __init__(self, nombre:str, descripcion:str):

        if not isinstance(nombre, str):
            raise ValueError("[!] El nombre no es un string")
        if not isinstance(descripcion, str):
            raise ValueError("[!] La descripcion no es un string")
        
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__participantes = []

    def __str__(self):
        return f"Disciplina: {self.__nombre} Description: {self.__descripcion} Participantes: {len(self.__participantes)}"
    
    def __repr__(self):
        return f"({self.__nombre},{self.__descripcion})"
    
    #Los <<Comandos>>
    def establecerNombre(self, nombre:str):
        self.__nombre = nombre

    def establecerDescripcion(self, descripcion:str):
        self.__descripcion = descripcion

    def agregarParticipante(self, participante:'Participante'):

        if participante not in self.__participante:
            self.__participantes.append(participante)


    #Las <<Consultas>>
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerDescripcion(self) -> str:
        return self.__descripcion
    
    def obtenerParticipantes(self) -> list:
        return self.__participantes
    

#Clase TESTER
class tester:
    @staticmethod
    def test():

        futbol = Disciplina("Futbol", "11v11 Pelota redoanda")
        basket = Disciplina("Basket", "5v5 Pelota redoanda")
        rugby = Disciplina("rugby", "15v15 Pelota redoanda")
        participante1 = Participante("Franco", 19, "Italiano")

        print(participante1)
        print(participante1.obtenerDisciplinas())

        participante1.agregarDisciplina(futbol)
        participante1.agregarDisciplina(rugby)
        print(participante1.obtenerDisciplinas())

        print(futbol.obtenerParticipantes())


if __name__ == '__main__':
    tester.test()
       