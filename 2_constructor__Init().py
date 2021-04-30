class hero:
    def __init__(self,inputNama,inputPower,inputRace):
        self.name=inputNama
        self.power=inputPower
        self.race=inputRace


hero1 = hero("Andru",10000000,"Demon")
hero2 = hero("Anggi",10000,"Angel")
hero3 = hero("Hanvir",100,"Human")

print(hero1.name)
print(hero1.power)
print(hero1.race)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)