class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):  # method of object x
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age) # it will make the child class inherit all the methods and properties from its parent:
        #adding property in Student class
        self.graduationyear = year

        # add methods to student class
    def welcome(self):
        print("Welcome", self.name, self.age, "to the class of ", self.graduationyear)

# x = Person("Suman", 20) # object
# x = Student("Steve", 31)
x = Student("Steve", 31, 2024)
# x.printName() 
# print(x.graduationyear)   # printing added property in child class
x.welcome() # printing added method



