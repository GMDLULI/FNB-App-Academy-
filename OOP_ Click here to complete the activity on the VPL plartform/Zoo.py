class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def makeSound(self):
        print(f"My name is {self.name} and I am {self.age} years old")


class Snake(Animal):

    def __init__(self, name, age, length):
        super().__init__(name, age)
        self.length = length

    def makeSound(self):
        print(f"I am a snake and i go SSSSSSS ")


class Lion(Animal):

    def __init__(self, name, age, fColor):
        super().__init__(name, age)
        self.furrcolor = fColor

    def makeSound(self):
        print("I am a lion and i go ROAR")

    def run(self, runSpeed):
        print(f"I am {self.name} and i am running at a speed of {runSpeed} km/h")


class Elephant(Animal):

    # TODO 1: Call the parent class's __init__ using super(),
    # passing name and age, then set self.trunkLength

    def __init__(self, name, age, trunkLength):
        super().__init__(name, age)
        self.trunkLength = trunkLength

    # TODO 2: Override makeSound() so it:
    #   - calls the base class's makeSound() using super()
    #   - then prints "GORRRRRRR"
    def makeSound(self):
        super().makeSound()
        print("GORRRRRRR")


class ZOO:

    def __init__(self, name, animals):
        self.name = name
        self.animals = animals

    # TODO 3: complete this method so animals can be added after the Zoo is created

    def addAnimal(self, addAnimal):
        self.animals.append(addAnimal)

    # TODO 4: complete this method so animals can be removed after creation

    def removeAnimal(self, addAnimal):
        self.animals.remove(addAnimal)


def demo():
    L1 = Lion("Bob", 20, "yellow")
    S1 = Snake("Steve", 15, 900)

    listAnimal = [L1, S1]

    Z1 = ZOO("Johannesburg Zoo", listAnimal)

    for A in Z1.animals:
        A.makeSound()

    print("--------END OF TEST 1--------")

    # TODO 5: Create an instance of Elephant and add it to the zoo
    # using the addAnimal() method provided

    elephant = Elephant("Dumbo", 10, 150)
    Z1.addAnimal(elephant)

    # If correctly defined, this second loop should now also print
    # the elephant's info and its sound
    for A in Z1.animals:
        A.makeSound()

    print("--------END OF TEST 2--------")

    # If removeAnimal is correctly defined the loop below should print
    # for every animal except the lion

    Z1.removeAnimal(L1)

    for A in Z1.animals:
        A.makeSound()

    print("--------END OF TEST 3--------")

    return Z1

demo()
