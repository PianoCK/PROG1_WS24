class Kaffeemaschine:
    def __init__(self, name):
        self.name = name
        self.kaffeesorten = {'Crema': 0,
                        'Cappuchino': 0,
                        'Americano': 0,
                        'Espresso': 0,
                        'Latte Macchiato': 0,
                        'Milchkaffee': 0}
        
    def zubereiten(self, sorte):  
        if sorte in self.kaffeesorten:
            print(f"Gute Wahl. Sie haben {sorte} gewählt.") 
            self.kaffeesorten[sorte] += 1
        else:
            print(f"Die Sorte {sorte} existiert nicht.") 

    def zweites_item(self, e):
        return e[1]

    def bildschirm_ki(self):
        items = self.kaffeesorten.items()
        items_sortiert = sorted(items,key=self.zweites_item,reverse=True)
        for index in range(4):
            print(f"{index+1}: {items_sortiert[index][0]}")
        
    def anzeigen_kaffeesorten(self):
        print(f"** {self.name} KAFFEEMASCHINE **")
        print("Hier ist die Auswahl an Kaffeesorten:")
        for kaffeesorte in self.kaffeesorten:
            print(kaffeesorte)

jura = Kaffeemaschine("JURA ENA 8")
jura.anzeigen_kaffeesorten()
jura.zubereiten("Espresso")
jura.zubereiten("Espresso")
jura.zubereiten("Espresso")
jura.zubereiten("Latte Macchiato")
jura.zubereiten("Crema")
jura.zubereiten("Crema")
jura.zubereiten("Espresso")
jura.zubereiten("Espresso")
jura.zubereiten("Crema")
jura.zubereiten("Crema")
jura.zubereiten("Cappuchino")
jura.zubereiten("Cappuchino")
jura.bildschirm_ki()
