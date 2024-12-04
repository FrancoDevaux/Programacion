class Atleta:

    #<<Atributos de clase>>
    MAX_VALOR = 100
    MIN_VALOR = 1


    #<<Constructor>>
    def __init__(self,nombre:str) -> None:

        if not isinstance(nombre,str):
            raise ValueError("[!]El nombre no es un string")
        
        #Los atributos de instancia
        self.__nombre = nombre
        self.__energia = Atleta.MAX_VALOR
        self.__destreza = Atleta.MIN_VALOR 
        self.__cantEntrenamientos = 0

    
    def __str__(self) -> str:
        return f"\n[+]Atleta: {self.__nombre}, Energia: {self.__energia}, Destreza: {self.__destreza}"
    

    #<<Consultas Triviales>>
    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerEnergia(self):
        return self.__energia
    
    def obtenerDestreza(self):
        return self.__destreza
    

    #<<Comandos Triviales>>
    def establecerEnergia(self,x:int):

        if not isinstance(x,int) or x > Atleta.MAX_VALOR or x < Atleta.MIN_VALOR:
            print(f"\n[!]Erro al ingresar la energia..")
            return  #Esto significa que la función termina sin devolver nada (técnicamente, devuelve el valor None).
        self.__energia = x

    def establecerDestreza(self,x:int):

        if not isinstance(x,int) or x > Atleta.MAX_VALOR or x < Atleta.MIN_VALOR:
            print(f"\n[!]Erro al ingresar la destreza..")
            return
        self.__destreza = x
        
    def entrenar(self) -> bool:
        
        if self.__energia <= 5:
            print(f"\n{self.__nombre} no tienes suficiente energia para entrenar, SORRY")
            return False
        
        print(f"\n[+]{self.__nombre} entrena")
        if self.__energia - 5 > Atleta.MIN_VALOR:
            self.__energia -= 5
        else:
            self.__energia = Atleta.MIN_VALOR

        self.__cantEntrenamientos += 1

        if self.__cantEntrenamientos >= 5:
            self.__destreza += 1
            self.__cantEntrenamientos = 0

        return True
        
    def descansar(self):
        print(f"\n{self.__nombre} descansa")
        if self.__energia + 20 < Atleta.MAX_VALOR:
            self.__energia += 20
        else:
            self.__energia = Atleta.MAX_VALOR

        

    #<<Consultas del ejercicio>>
    def mismaDestrezaQue(self,otroAtleta:'Atleta') -> bool:
        return otroAtleta.obtenerDestreza() == self.__destreza
    
    def mayorDestrezaQue(self,otroAtleta:'Atleta') -> bool:
        return self.__destreza > otroAtleta.obtenerDestreza()
    


    # -------------------------------Clase Tester------------------------------------

class TesterAtleta:
    @staticmethod
    def test():

        atleta1 = Atleta("Jorge")
        print(atleta1)

        for i in range(20):
            atleta1.entrenar()
            print(atleta1)

        for i in range(3):
            atleta1.descansar()
            print(atleta1)

        atleta1.establecerEnergia("Enderperl")
        atleta1.establecerDestreza(30)
        print(atleta1)


        atleta2 = Atleta("Roberto")

        if atleta1.mayorDestrezaQue(atleta2):
            print(f"\n[+]{atleta1.obtenerNombre()} tiene mayor destreza que {atleta2.obtenerNombre()}")
        else:
            print(f"\n[-]{atleta1.obtenerNombre()} NO tiene mayor destreza que {atleta2.obtenerNombre()}")

        if atleta1.mismaDestrezaQue(atleta2):
            print(f"\n[+]{atleta1.obtenerNombre()} tiene la misma destreza que {atleta2.obtenerNombre()}")
        else:
            print(f"\n[-]{atleta1.obtenerNombre()} NO tiene la misma destreza que {atleta2.obtenerNombre()}")


if __name__ == "__main__":
    TesterAtleta.test()






