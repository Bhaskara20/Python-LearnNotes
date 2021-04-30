class Hero:

    #inisiasi
    def __init__(self,Nama,Kekuatan,Kesehatan):
        #variabel utama(bersifat private)
        self.__name=Nama
        self.__power=Kekuatan
        self.__health=Kesehatan
    
    #Getter
    def getName(self):
        return self.__name
    
    def getPower(self):
        return self.__power
    
    def getHealth(self):
        return self.__health

    #setter
    def hurt(self, damage):
        self.__health-=damage
    
    def powerUp(self, upgrade):
        self.__power+=upgrade


#running program 
Andru=Hero("Andru",100,60)
print(Andru.__dict__)
print("Name : ",Andru.getName())
print("Power : ",Andru.getPower())
print("Health : ",Andru.getHealth())

Andru.hurt(10)
print("Health : ",Andru.getHealth())

Andru.powerUp(100)
print("Power : ",Andru.getPower())


