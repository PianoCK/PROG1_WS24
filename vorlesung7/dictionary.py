meine_bibliothek = {}

meine_bibliothek["Star Wars"] = 9.7
meine_bibliothek["Indiana Jones"] = 9.5
meine_bibliothek["Der Postmann"] = 2.6

for element in meine_bibliothek:
    if meine_bibliothek[element] >= 9:
        print(element, meine_bibliothek[element])