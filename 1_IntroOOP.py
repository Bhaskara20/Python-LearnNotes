class hero:
    pass

hero1=hero()
hero2=hero()
hero3=hero()

hero1.name="Andru"
hero1.race="Demon"
hero1.power="1000000"

hero2.name="Anggi"
hero2.race="Angel"
hero2.power="10000"

hero3.name="Han"
hero3.race="Human"
hero3.power="100"

print(hero1)
print(hero1.__dict__)
print("Nama : ",hero1.name)
print("Ras : ",hero1.race)
print("Kekuatan : ",hero1.power)
