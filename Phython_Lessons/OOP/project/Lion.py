from Animal import Animal

class Lion(Animal):
    def __init__(self, name, age, number_claws):
        super().__init__(name, age)
        self.number_claws = number_claws

    def make_sound(self): # method overriding - same method name as the parent class but different implementation
        print(f"Roar! Hi my name is {self.name} and I am {self.age} years old and I am a lion with {self.number_claws} claws")