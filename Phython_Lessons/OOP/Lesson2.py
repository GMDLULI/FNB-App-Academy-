class RobotAnimal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class RobotDog(RobotAnimal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def display(self):
        super().display()
        print(f"I am a Dog and I have a Color: {self.color}")

class RobotCat(RobotAnimal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def display(self):
        super().display()
        print(f"I am a Cat and I have a Color: {self.color}")

class RobotZoo():
    def __init__(self, animal):
        self.animal = animal
    def visit(self):
        self.animal.display()
        f=open("ZooNotes.txt", "w")
        f.write(f"Visited {self.animal.name}")
        f.close()   

dog = RobotDog("Rex", 5, "Brown")
cat = RobotCat("Whiskers", 3, "Black")
zoo = RobotZoo(dog)

zoo.visit()

# print(f"Dog Name: {dog.name}, Age: {dog.age}, Color: {dog.color}")
# print(f"Cat Name: {cat.name}, Age: {cat.age}, Color: {cat.color}")
# dog.display()
# cat.display()

