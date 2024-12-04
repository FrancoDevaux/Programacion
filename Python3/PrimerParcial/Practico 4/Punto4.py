class MascotaVirtual:
    MAX = 100
    MIN = 0

    def __init__(self,nombre:str):

        self.__nombre = nombre
        self.__energia = MascotaVirtual.MAX
        self.__diversion = MascotaVirtual.MAX
        self.__higiene = MascotaVirtual.MAX
        self.__dormido = False
        self.__cantActividadesDesgaste = 0

    def __str__(self):
        
        return f"Nombre: {self.__nombre}\nEnergia: {self.__energia}\nDiversion: {self.__diversion}\nHigiene: {self.__higiene}\nDormdio: {self.__dormido}"
        

    #---------------------------------------------Los <<comandos>>---------------------------------------------------------

    def comer(self):
        if self.estaVivo():
            if not self.__dormido:
                if self.__energia + 20 < MascotaVirtual.MAX:
                    self.__energia += 20
                
                else:
                    self.__energia = MascotaVirtual.MAX

                print(f"\nEl {self.__nombre} comio")
                self.__cantActividadesDesgaste = 0

            else:
                print("\n[-]No puede comer porque esta durmiendo...")

    
    def beber(self):
        if self.estaVivo():
            if not self.__dormido:
                if self.__energia + 10 < MascotaVirtual.MAX:
                    self.__energia += 10

                else:
                    self.__energia = MascotaVirtual.MAX

                print(f"\nEl {self.__nombre} bebio")
                self.__cantActividadesDesgaste = 0
            
            else:
                print("\n[-]No puede beber porque esta durmiendo...")

            

    def dormir(self):
        if self.estaVivo():
            if self.__dormido:
                print(f"\nYa esta durmiendo")
            
            else:
                self.__dormido = True
                print(f"\nEl {self.__nombre} se durmio")

            self.__cantActividadesDesgaste = 0


    def despertar(self):
        if self.estaVivo():
            if self.__dormido:
                self.__dormido = False
                print(f"\nEl {self.__nombre} se acaba de despertar")

            else:
                print(f"Actualmente ya estaba despierto")


    def jugar(self):
        if self.estaVivo():
            if not self.__dormido:

                if self.__diversion + 40 < MascotaVirtual.MAX:
                    self.__diversion += 40
                else:
                    self.__diversion = MascotaVirtual.MAX

                if self.__energia - 20 > MascotaVirtual.MIN:
                    self.__energia -= 20
                else:
                    self.__diversion = MascotaVirtual.MIN

                if self.__higiene - 15 > MascotaVirtual.MIN:
                    self.__higiene -= 15
                else:
                    self.__higiene = MascotaVirtual.MIN


                #No puede hacer mas de 3 actividades
                self.__cantActividadesDesgaste += 1
                print (f"\nEl {self.__nombre} jugó")

                if self.__cantActividadesDesgaste >= 3:
                    self.dormir()

                return True
            
            else:
                print(f"\n[-]No puede jugar, esta durmiendo...")
                return False
            


    def caminar(self):
        if self.estaVivo():
            if not self.__dormido:

                if self.__diversion + 20 < MascotaVirtual.MAX:
                    self.__diversion += 20
                else:
                    self.__diversion = MascotaVirtual.MAX

                if self.__energia - 10 > MascotaVirtual.MIN:
                    self.__energia -= 10
                else:
                    self.__energia = MascotaVirtual.MIN

                if self.__higiene - 8 > MascotaVirtual.MIN:
                    self.__higiene -= 8
                else:
                    self.__higiene = MascotaVirtual.MIN


                self.__cantActividadesDesgaste += 1
                print (f"\nEl {self.__nombre} jugó")

                if self.__cantActividadesDesgaste >= 3:
                    self.dormir()

                return True
            
            else:
                print(f"\n[-]No puede caminar, esta durmiendo...")
                return False



    def saltar(self):
        if self.estaVivo():
            if not self.__dormido:

                if self.__diversion + 10 < MascotaVirtual.MAX:
                    self.__diversion += 10
                else:
                    self.__diversion = MascotaVirtual.MAX

                if self.__energia - 15 > MascotaVirtual.MIN:
                    self.__energia -= 15
                else:
                    self.__energia = MascotaVirtual.MIN

                if self.__higiene - 10 > MascotaVirtual.MIN:
                    self.__higiene -= 10
                else:
                    self.__higiene = MascotaVirtual.MIN


                self.__cantActividadesDesgaste += 1
                print (f"\nEl {self.__nombre} jugó")

                if self.__cantActividadesDesgaste >= 3:
                    self.dormir()

                return True
            
            else:
                print(f"\n[-]No puede saltar, esta durmiendo...")
                return False
                

    def bañar(self):
        if self.estaVivo():
            if not self.__dormido:

                if self.__higiene + 40 < MascotaVirtual.MAX:
                    self.__higiene += 40
                else:
                    self.__higiene = MascotaVirtual.MAX

                if self.__diversion - 10 > MascotaVirtual.MIN:
                    self.__diversion -= 10
                else:
                    self.__diversion = MascotaVirtual.MIN


                print(f"\nEl {self.__nombre} se bañó")
                self.__cantActividadesDesgaste = 0
            
            else:
                print("\n[-]No puede bañar porque esta durmiendo...")


    #--------------------------------------------Las <<consultas>>---------------------------------------------

    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerEnergia(self)->int:
        return self.__energia
    
    def obtenerDiversion(self)->int:
        return self.__diversion
    
    def obtenerHigiene(self)->int:
        return self.__higiene
    
    def estaDormiedo(self)->bool:
        return self.__dormido
    
    def obtenerHumor(self)->str:

        energia = self.__energia
        diversion = self.__diversion
        higiene = self.__higiene


        if energia >= 70 and diversion >= 70 and higiene >= 70:
            return f"\n[+]Humor Feliz"

        elif (50 <= energia >= 70 and 50 <= diversion >= 70) or (50 <= energia >= 70 and 50 <= higiene >= 70) or (50 <= diversion >= 70 and 50 <= higiene >= 70):
            return f"\n[+]Humor alegre"

        elif (30 <= energia >= 50 and 30 <= diversion >= 50) or (30 <= energia >= 50 and 30 <= higiene >= 50) or (30 <= diversion >= 50 and 30 <= higiene >= 50):
            return f"\n[+]Humor neutral"

        elif (10 <= energia >= 30 and 10 <= diversion >= 30) or (10 <= energia >= 30 and 10 <= higiene >= 30) or (10 <= diversion >= 30 and 10 <= higiene >= 30):
            return f"\n[-]Humor Triste"
         
        else:
            return f"\n[--]Humor Muy Triste"

    def estaVivo(self)->bool:
        if self.__energia == MascotaVirtual.MIN:
            print(f"\nEl {self.__nombre} esta enterrado bajo tierra")
            return False
        else:
            return True


#----------------------------------Clase Tester---------------------------------------

class TesterMascotaVirtual:
    @staticmethod

    def test():

        Tamagochi = MascotaVirtual("Tamagochi")
        Tamagochi.jugar()
        Tamagochi.jugar()
        Tamagochi.saltar()
        Tamagochi.caminar()
        print(Tamagochi)
        Tamagochi.jugar()

if __name__ == "__main__":
    TesterMascotaVirtual.test()


