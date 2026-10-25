from Animal import Animal

class Snake(Animal):
    def __init__(self, name, age, venomPotency):
        super().__init__(name, age)
        self.venomPotency = venomPotency

    def make_sound(self): # method overriding - same method name as the parent class but different implementation
        print(f"SSSSSSS Hi my name isssssss {self.name} and I am {self.age} yearsssss old and I am a snake with a venom potency of {self.venomPotency}")