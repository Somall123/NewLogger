import random

class Logger:
    def Log(self,x):
        print(x)

class Person:
    Name = None
    Age = None

    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def stringify(self):
        return "Name Is:", self.Name, " Age is:", self.Age

def generate_people(amount):
    names = ["Daviti", "NikaBuzalaa", "Miha", "MrFrostiko", "VakhoLektori", "SomalaMoswavle"]
    random.shuffle(names)
    persons = []
    for _ in range(amount):
        name = random.choice(names)
        age = random.randrange(15, 18)
        persons.append(Person(name, age))
    return persons

people = generate_people(3)
lgrr=Logger()
for person in people:
    lgrr.Log(person.stringify())