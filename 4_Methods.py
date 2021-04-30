class hero:
    #class variable
    jumlah=0
    def __init__(self,inputNama,inputPower,inputRace):
        #instance variable
        self.name=inputNama
        self.power=inputPower
        self.race=inputRace
        hero.jumlah+=1
    
    def powerUp(self,UP):
        print("Kekuatan bertambah sebesar ",UP)
        self.power+=UP
        print(self.power)
    
    def whoamI(self):
        print("Nama ku adalah ",self.name)
    
    def getInformasiRas(self):
        return print("Ras : ",self.race)

hero1 = hero("Andru",10000000,"Demon")

hero1.whoamI()
hero1.powerUp(1)
hero1.getInformasiRas()



