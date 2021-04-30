class hero:
    #class variable
    jumlah=0
    def __init__(self,inputNama,inputPower,inputRace):
        #instance variable
        self.name=inputNama
        self.power=inputPower
        self.race=inputRace
        hero.jumlah+=1
        print("Hero ",inputNama," telah dibuat!")


hero1 = hero("Andru",10000000,"Demon")
print("Jumlah hero : ",hero.jumlah)
hero2 = hero("Anggi",10000,"Angel")
print("Jumlah hero : ",hero.jumlah)
hero3 = hero("Hanvir",100,"Human")
print("Jumlah hero : ",hero.jumlah)

