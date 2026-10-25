from Animal import Animal

class Elephant(Animal):
    def __init__(self, name, age, tusk_length):
        super().__init__(name, age)
        self.tusk_length = tusk_length

    def make_sound(self): # method overriding - same method name as the parent class but different implementation
        print(f"Hi my name is {self.name} and I am {self.age} years old and I am an elephant with a tusk length of {self.tusk_length} meters")