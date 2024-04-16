import random
levels={
    "info":0,
    "warning":1,
    "debug":2
}

class Logger:
    def __init__(self):
        self.log_level=levels["info"]
    def Log(self,x):
        print(x)
    def info(self, message):
        if self.log_level == levels["info"]:
            print(message)
    def warning(self, message1):
        if self.log_level == levels["warning"]:
            print(message1)
    def debug(self, message2):
        if self.log_level == levels["debug"]:
            print(message2)
        

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


if(levels.level ==0):
    print("There is a problem")
