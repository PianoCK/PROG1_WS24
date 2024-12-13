class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(\"{self.name}\")"

class Student(Person):
    def __repr__(self):
        return f"Student(\"{self.name}\")"
    
    def show_deutschlandticket(self):
        print("Bahnticket 1234")

person1 = Student("Maria")
person2 = Person("Peter")
person1.show_deutschlandticket()
print(person2.name)
print(person1.name)
print(person1)
print(person2)

