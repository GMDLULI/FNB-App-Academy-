class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"Hi my name is {self.name} and I am {self.age} years old")