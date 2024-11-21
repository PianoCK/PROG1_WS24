meine_liste = ["Hallo", 3.7, True, 312, "Anna"]


def finde_in_liste(wert) -> bool:
    for element in meine_liste:
        if element == wert:
            return True
    return False

print(len(meine_liste)) # Länge der Liste
print("Anna" in meine_liste) # 
print(finde_in_liste("Annabell"))