# Polymorphism in Python

class Zoo:
    def __init__(self,name, aniamals):
        self.name = name
        self.aniamals = aniamals # composition - has a relationship with the animal class takes in animal class as a parameter


class Animal:
    def __init__(self,name, age):
        self.name = name
        self.age = age


    def speak(self):
        print(f"Hi my name is {self.name} and I am {self.age} years old")

class Snake(Animal):
    def __init__(self, name, age, length):
        super().__init__(name, age)
        self.length = length

    def speak(self): #method overriding - same method name as the parent class but different implementation
        print(f"SSSSSSS Hi my name isssssss {self.name} and I am {self.age} yearsssss old and I am a snake with a length of {self.length} metersssss")

    

dog = Animal("Bob", 5)
snake = Snake("Slytherin", 2, 5)

list_of_animals = [dog, snake]

zoo1 = Zoo("My Zoo", list_of_animals)

for animal in zoo1.aniamals:
    animal.speak()