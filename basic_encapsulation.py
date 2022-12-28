class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def setName(self, n):
            self.name = n

    def setAge(self, a):
        if(a>0):
            self.age = a

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


person = Person()
person.setName("suman")
person.setAge(20)

print(f"Name : {person.getName()}")
print(f"Age : {person.getAge()}")

