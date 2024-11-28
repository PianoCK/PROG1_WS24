class Auto:
    anzahl_autos = 0

    def __init__(self, autoname):
        #print("Ich bin gerade aus der Konstruktion gekommen! Hurra!")
        self.__kmstand = 0
        self.name = autoname
        Auto.anzahl_autos += 1

    def fahren(self, km):
        if km > 0:
            self.__kmstand += km

    def get_kmstand(self):
        print(f"Das Auto {self.name} hat den KmStand: {self.__kmstand}")

    def wer_bin_ich(self):
        print(f"Ich bin ein Auto an der Adresse {id(self)}")

    def __del__(self):
        print(f"{self.name} wurde auf den Schrottplatz gefahren")
        Auto.anzahl_autos -= 1

print(Auto.anzahl_autos)
auto1 = Auto("VW Beetle")
auto2 = Auto("BMW X7")
print(Auto.anzahl_autos)
auto1.__kmstand = 5000
auto1.fahren(50)
auto1.get_kmstand()
del auto1
print(Auto.anzahl_autos)
auto2.get_kmstand()