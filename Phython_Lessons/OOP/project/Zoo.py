
import json

from Lion import Lion
from Elephant import Elephant
from Snake import Snake
class Zoo:

    def __init__(self, name, entryCost):
        self.name = name
        self.entryCost = entryCost
        self.animals = []
        self.number_of_visits = 0
        self.load_animals(False)


    def load_animals(self, flag):
        try:
            with open('zooAnimals.json', 'r') as f:
                listObj = json.load(f)
            if flag:
                return listObj
            else: 
                for A in listObj:
                    self.add_animal(A,True)
        except FileNotFoundError as e:
            print(f"File not found: {e.filename}")
            return [{}]

    def add_animal(self, animalInfo, flagLoad):
        if animalInfo.get('type') == 'Lion':
            animal = Lion(animalInfo.get('name'), animalInfo.get('age'), animalInfo.get('number_claws'))
            self.animals.append(animal)
            if flagLoad:
                return
            newListDict = self.load_animals(True)
            newListDict.append(animalInfo)
            self.store_animals(newListDict)
        elif animalInfo.get('type') == 'Elephant':
            animal = Elephant(animalInfo.get('name'), animalInfo.get('age'), animalInfo.get('tusk_length'))
            self.animals.append(animal)

            newListDict = self.load_animals(True)
            newListDict.append(animalInfo)
            self.store_animals(newListDict)
        elif animalInfo.get('type') == 'Snake':
            animal = Snake(animalInfo.get('name'), animalInfo.get('age'), animalInfo.get('venomPotency'))
            self.animals.append(animal)
            newListDict = self.load_animals(True)
            newListDict.append(animalInfo)
            self.store_animals(newListDict)

    def store_animals(self, animalInfo):
        try:
            with open('zooAnimals.json', 'w') as f:
                    json.dump(animalInfo, f)
        except FileNotFoundError as e:
            print(f"File not found: {e.filename}")

    
    def visit_animal(self, animalType):
        found = False

        for animal in self.animals:
            if type(animal).__name__ == animalType:
                animal.make_sound()
                self.number_of_visits += 1
                found = True

        if not found:
            print(f"No {animalType} found in the zoo.")
    def show_stats(self):
        print(f"Zoo Name: {self.name}")
        print(f"Entry Cost: {self.number_of_visits * self.entryCost}")
        print("Animals in the Zoo:")
        for animal in self.animals:
            print(f"- {type(animal).__name__}: {animal.name}, Age: {animal.age}")


   