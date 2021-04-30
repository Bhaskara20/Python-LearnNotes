class Hero:
    def __init__(self,inputNama,inputSerangan,inputPertahanan,inputSehat):
        self.health=inputSehat
        self.name=inputNama
        self.attack=inputSerangan
        self.defense=inputPertahanan
    
    def serang(self,enemy):
        print(self.name, " Attack ",enemy.name)
        enemy.pertahanan(self)
    

    def pertahanan(self,enemy):
        print(self.name," dealt damage from ",enemy.name)
        jumlahSerangan=enemy.attack/self.defense
        print("Serangan yang diterima sebesar ",jumlahSerangan)
        sisaSehat=self.health-jumlahSerangan
        print(self.name," memiliki sisa darah sebanyak ",int(sisaSehat))



Andru=Hero("Andru",20, 30, 900)
wahyu=Hero("Wahyu",10,18,300)

Andru.serang(wahyu)
wahyu.serang(Andru)


