import random
richtige_tipps = 0
spiele = 3
for spiel in range(1,spiele+1):
    zahl1 = random.randint(1,10)
    zahl2 = random.randint(1,10)
    ergebnis = zahl1 + zahl2
    print("\nSpiel Nr.", spiel)
    while True:
        try:
            tipp = int(input(f"Was ist {zahl1} + {zahl2}? "))
            if ergebnis == tipp:
                print("Das war richtig!")
                richtige_tipps += 1
            else:
                print(f"Das war leider falsch. Richtig wäre {ergebnis}")
            break
        except:
            print("Das war keine Zahl als Eingabe.")
print("----------------")
print("** Auswertung **")
print("----------------")
print(f"{richtige_tipps} von {spiele} waren richtig.")
