class Color:

    def __init__(self, rojo:int=255, verde:int=255, azul:int=255):

        for color in [rojo,verde,azul]:
            if not isinstance(color,int) or color > 255 or color < 0:
                raise ValueError("Error al ingresar datos")
            
        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul

    def __str__(self) -> str:
        return f"Color RGB: ({self.__rojo}, {self.__verde}, {self.__azul})"
    
    def __repr__(self) -> str:
        return f"Color({self.__rojo},{self.__verde},{self.__azul})"
    
    #<<Consultas>>
    def obtenerRojo(self) -> int:
        return self.__rojo
    
    def obtenerVerde(self) -> int:
        return self.__verde
    
    def obtenerAzul(self) -> int:
        return self.__azul
    
    def obtenerRGB(self) -> tuple:
        return self.__rojo, self.__verde, self.__azul
    
    def esRojo(self) -> bool:
        """
        retorna el valor verdadero si el objeto que recibe por mensaje representa el color rojo
        RETURNS:
            bool: __descripcion__
        """
        return self.__rojo == 255 and self.__verde == 0 and self.__azul == 0
    
    def esNegro(self) -> bool:
        """
        retorna el valor verdadero si el objeto que recibe por mensaje representa el color negro
        RETURNS:
            bool: __descripcion__
        """
        return self.__rojo == 255 and self.__verde == 255 and self.__azul == 255
    
    def esGris(self) -> bool:
        """
        retorna el valor verdadero si el objeto que recibe por mensaje representa el color gris
        RETURNS:
            bool: __descripcion__
        """
        return self.__rojo == self.__verde == self.__azul
    
    def complemento(self) -> "Color":
        """
        retorna un nuevo objeto con el color complemento del color del objeto que recibe el mensaje para alcanzar el color blanco.
        RETURNS:
            Color: __descripcion__
        """
        return Color(255 - self.__rojo, 255 - self.__verde, 255 - self.__azul)
    
    def esIgualQue(self, otroColor:"Color") -> bool:
        """
        retorna el valor verdadero si ambos objetos son equivalentes.
        """
        return self.__rojo == otroColor.obtenerRojo() and self.__verde == otroColor.obtenerVerde() and self.__azul == otroColor.obtenerAzul()
    
    def clonar(self) -> "Color":
        """
        devuelve un nuevo color con el mismo estado interno que el color que recibe el mensaje.
        """
        return eval(self.__repr__()) 
    

    # <<Comandos>>

    def variar(self, val:int):
        """
        modifica cada componente de color sumándole si es posible, un valor dado. 
        Si sumándole el valor dado a una o varias componentes se supera el valor 255, 
        dicha componente queda en 255. Si el argumento es negativo la operación es la misma 
        pero en ese caso el mínimo valor que puede tomar una componente, es 0.
        """
        self.variarRojo(val)
        self.variarVerde(val)
        self.variarAzul(val)

    def variarRojo(self, val:int):
        """
        modifica la componente de rojo sumándole un valor dado. 
        Ídem para azul (variarAzul(val:entero)) y verde (variarVerde(val:entero)).
        """
        if val > 0:
            if self.__rojo + val < 255:
                self.__rojo += val
            else:
                self.__rojo = 255
        elif val < 0:
            if self.__rojo + val > 0:
                self.__rojo += val
            else:
                self.__rojo = 0

    def variarVerde(self, val:int):
        """
        modifica la componente de verde sumándole un valor dado.
        """
        if val > 0:
            if self.__verde + val < 255:
                self.__verde += val
            else:
                self.__verde = 255
        elif val < 0:
            if self.__verde + val > 0:
                self.__verde += val
            else:
                self.__verde = 0

    def variarAzul(self, val:int):
        """
        modifica la componente de azul sumándole un valor dado.
        """
        if val > 0:
            if self.__azul + val < 255:
                self.__azul += val
            else:
                self.__azul = 255
        elif val < 0:
            if self.__azul + val > 0:
                self.__azul += val
            else:
                self.__azul = 0

    def establecerRojo(self, val:int):
        
        if isinstance(val, int) and val >= 0 and val <= 255:
            self.__rojo = val
  
    def establecerVerde(self, val:int):
        
        if isinstance(val, int) and val >= 0 and val <= 255:
            self.__verde = val

    def establecerAzul(self, val:int):  
        
        if isinstance(val, int) and val >= 0 and val <= 255:
            self.__azul = val

    def copiar(self, otroColor:"Color"):
    
        self.__rojo = otroColor.obtenerRojo() 
        self.__verde = otroColor.obtenerVerde()
        self.__azul = otroColor.obtenerAzul()

    
    class TesterColores:
        
        @staticmethod
        def test():
            
            color1 = Color(255, 0, 0)
            print(color1)
            
            color2 = Color(0, 255, 0)
            print(color2)
            
            color3 = Color(0, 0, 255)
            print(color3)
        
    

if __name__ == "__main__":
    Color.TesterColores.test()
        
