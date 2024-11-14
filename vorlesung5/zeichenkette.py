todo = ["Aufwachen","Zähne putzen"]
todo.append("Einkaufen")
todo.append("Python lernen")
todo.append("Sport")

for index in range(len(todo)):
    if todo[index] == "Einkaufen":
        index_merken = index
todo.insert(index_merken, "Geld abheben")

print(todo)