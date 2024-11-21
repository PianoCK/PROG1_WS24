meine_bibliothek = {}
meine_bibliothek["Star Wars"] = 9.7
meine_bibliothek["Indiana Jones"] = 9.5
meine_bibliothek["Der Postmann"] = 2.6

meine_filmliste = [["Star Wars", 9.7], 
                   ["Indiana Jones", 9,5], 
                   ["Der Postmann", 2.6]]

# Dies ist gleichbedeutend
if "Star Trek" in meine_bibliothek:
    print(meine_bibliothek["Star Trek"])
meine_bibliothek["Der Postmann"] = 2.1
print(meine_bibliothek["Indiana Jones"]) # O(1)
for element in meine_filmliste:          # O(n)
    if element[0] == "Indiana Jones":
        print(element)

for element in meine_bibliothek:
    if meine_bibliothek[element] >= 9:
        print(element, meine_bibliothek[element])