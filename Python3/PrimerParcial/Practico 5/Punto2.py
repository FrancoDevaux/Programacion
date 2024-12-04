from datetime import time
class Fecha:

    def __init__(self, dia:int, mes:int, anio:int):

        if mes < 1 or mes > 12:
            raise ValueError("El mes debe estar entre 1 y 12")
        
        elif mes == 2 and dia > 28 and not self.__EsAnioBisiesto(anio):
            raise ValueError("El mes Febrero no puede tener mas de 28 dias")
        
        elif (mes == 4 or mes == 6 or mes == 9 or mes == 9 or mes == 11) and dia > 30:
            raise ValueError("El mes no puede tener mas de 30 dias")
        
        elif (mes == 1 or mes == 3 or mes == 5 or mes ==7 or mes == 8 or mes == 10 or mes == 12) and dia > 31:
            raise ValueError("El mes no puede tener mas de 31 dias")
    
        else:
            self.__dia = dia
            self.__mes = mes
            self.__anio = anio

    
    # Los <<Comandos>>

    def establecerDia(self, dia:int):
        self.__dia = dia

    def establecerMes(self, mes:int):
        self.__mes = mes

    def establecerAnio(self, anio:int):
        self.__anio = anio


    #Las <<Consultas>>

    def obtenerDia(self) -> int:
        return self.__dia
    
    def obtenerMes(self) -> int:
        return self.__mes
    
    def obtenerAnio(self) -> int:
        return self.__anio
    
    def esAnterior(self, otraFecha:"Fecha") -> bool:
        
        if self.__anio < otraFecha.obtenerAnio():
            return True
        
        elif self.__anio == otraFecha.obtenerAnio():
            if self.__mes < otraFecha.obtenerMes():
                return True
            elif self.__mes == otraFecha.obtenerMes():
                if self.__dia < otraFecha.obtenerDia():
                    return True
                
        else:
            return False
        
    def sumaDias(self, cantDias:int) -> "Fecha":

        dia = self.__dia
        mes = self.__mes
        anio = self.__anio

        while dia > self.__diasDelMes(mes):
            dia -= self.__diaDelMes(mes)
            mes += 1

            if mes < 12:
                mes = 1
                anio += 1
            return Fecha(dia, mes, anio)
        

    def diaSiguiente(self) -> "Fecha":
        return self.sumaDias(1)
    
    def esIgualQue(self, otraFecha:"Fecha") -> bool:
        return self.__dia == otraFecha.obtenerDia() and self.__mes == otraFecha.obtenerMes() and self.__anio == otraFecha.obtenerAnio()

    def __str__(self) -> str:
        return f"{self.__dia}/{self.__mes}/{self.__anio}" 
    
    def esAnioBisiesto(self) -> bool:
        return self.__anio % 4 == 0 and (self.__anio % 100 != 0 or self.__anio % 400 == 0)
    

# Clase TESTER

class tester:
    @staticmethod
    def test():

        try:
            fecha1 = Fecha(31,2,2022)  #no existe esta fecha
            print(fecha1)
        except ValueError as i:
            print(i)

        fecha2 = Fecha(30,7,2021)
        print(fecha2)

        fecha2.establecerDia(31)
        print(fecha2)


if __name__ == "__main__":
    tester.test()
