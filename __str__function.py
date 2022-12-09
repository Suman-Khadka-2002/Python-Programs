class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}({self.age})"


p1 = Person("Suman", 20)
print(p1)
