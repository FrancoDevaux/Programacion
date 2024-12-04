from abc import ABC, abstractmethod
from datetime import datetime

class Empleado(ABC):

    def __init__(self, nombre: str, apellido: str, dni: str, anioIngreso: int):

        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("[!] El nombre no es un string")
        if not isinstance(apellido, str) or apellido == "" or apellido.isspace():
            raise ValueError("[!] El apellido no es un string")
        if not isinstance(dni, str) or dni == "" or dni.isspace():
            raise ValueError("[!] El DNI no es válido")
        if not isinstance(anioIngreso, int) or anioIngreso < 0:
            raise ValueError("[!] El año de ingreso no es válido")
        
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._anioIngreso = anioIngreso

    
    @abstractmethod
    def calcularSalario(self) -> float:
        pass
    
    def nombreCompleto(self) -> str:
        return f"{self._apellido}, {self._nombre}"
    
    def antiguedadEnAnios(self) -> int:
        return datetime.now().year - self.__anioIngreso
    
    def __str__(self):
        return f"{self._dni} - {self._nombre} , {self._apellido} (Ingreso: {self._anioIngreso})"
    


class EmpleadoSalarioFijo(Empleado):

    __PORC_2_A_5 = 0.05
    __PORC_MAS_DE_5 = 0.1
    __ANIO_LIMITE_INFERIOR = 2
    ANIO_LIMITE_SUPERIOR = 5

    def __init__(self, nombre: str, apellido: str, dni: str, anioIngreso: int, sueldoBasico: float):
        super().__init__(nombre, apellido, dni, anioIngreso)

        if not isinstance(sueldoBasico, (int, float)) or sueldoBasico <= 0:
            raise ValueError("[!] El sueldo básico no es válido")
        self.__sueldoBasico = sueldoBasico


    def obtenerProcentajeAdicional(self) -> float:
        """
        El salario se obtiene multiplicando los clientes
        captados por el monto por cliente. Si el salario obtenido por los clientes captados no llega a
        cubrir el salario mínimo, entonces cobrará el salario mínimo.
        Los empleados con salario fijo tienen un sueldo básico y un porcentaje adicional en funcion
        del numero de años de antigüedad en la empresa: menos de dos años no cobran antigüedad,
        de 2 a 5 años cobran un 5% adicional, y más de 5 años cobran un 10% adicional.
        """
        
        porcentaje = 0
        if self.antiguedadEnAnios() > EmpleadoSalarioFijo.__ANIO_LIMITE_SUPERIOR:
            porcentaje = EmpleadoSalarioFijo.__PORC_MAS_DE_5
        elif self.antiguedadEnAnios() >= EmpleadoSalarioFijo.__ANIO_LIMITE_INFERIOR:
            porcentaje = EmpleadoSalarioFijo.__PORC_2_A_5
        
        return porcentaje
    
    def obtenerSalario(self) -> float:
        return self.__sueldoBasico + self.__sueldoBasico * self.obtenerProcentajeAdicional()
    
    def __str__(self):
        return f"{super().__str__()} - Sueldo: {self.obtenerSalario()}"


class EmpleadoAComision(Empleado):

    def __init__(self, nombre: str, apellido: str, dni: str, anioIngreso: int, salarioMinimo: float, cantClientesCapatados: int, montoPorCliente: float):
        super().__init__(nombre, apellido, dni, anioIngreso)
        
        if not isinstance(salarioMinimo, (int, float)) or salarioMinimo <= 0:
            raise ValueError("[!] El salario mínimo no es válido")
        if not isinstance(cantClientesCapatados, int) or cantClientesCapatados < 0:
            raise ValueError("[!] La cantidad de clientes captados no es válida")
        if not isinstance(montoPorCliente, (int, float)) or montoPorCliente < 0:
            raise ValueError("[!] El monto por cliente no es válido")
        
        self.__salarioMinimo = salarioMinimo
        self.__cantClientesCapatados = cantClientesCapatados
        self.__montoPorCliente = montoPorCliente


    def obtenerSalario(self) -> float:
        salario = self.__cantClientesCapatados * self.__montoPorClient
        if salario < self.__salarioMinimo:
            salario = self.__salarioMinimo
        return salario
    
    def obtenerClientesCapatados(self) -> int:
        return self.__cantClientesCapatados
    
    def __str__(self):
        return f"{super().__str__()} - Salario: {self.obtenerSalario()}, Clientes capatados: {self.__cantClientesCapatados}"
    

class Empresa():

    def __init__(self, lista=None):
        self.__listaEmpleados = [] 

    def agregarEmpleado(self, empleado:'Empleado'):
        if empleado not in self.__listaEmpleados:
            self.__listaEmpleados.append(empleado)