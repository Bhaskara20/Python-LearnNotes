class Hero:

    def __init__(self,inputNama,inputRace):
        #Public Methods
        self.name=inputNama
        self.race=inputRace

        #Private Methods
        self.__name="Baskara"
        self.__race="Human"

        #Protected Methods
        self._name="Putra"
        self._race="Elf"

Andru=Hero("Andru","Demon")
print(Andru.__dict__)
print(Andru.name)
print("\n")
print(Andru.__dict__)
#print(Andru.__name) #tidak dapat diakses karena private
print("\n")

print(Andru.__dict__)
print(Andru._name)