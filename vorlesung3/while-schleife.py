import random
summe = 0
zaehler = 0
while summe < 25:
    zaehler = zaehler + 1
    zufallszahl = random.randint(1,8)
    summe = summe + zufallszahl
    print(summe)

print("Anzahl Durchläufe:",zaehler)
print("Fertig.")

