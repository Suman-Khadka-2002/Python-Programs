# This is a basic example of __init__ function... which is called automatically everytime the class is being used to create a new object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Suman", 20)
print(p1.name)
print(p1.age)