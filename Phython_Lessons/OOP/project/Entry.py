from Zoo import Zoo


def main():

    menu = """
What would you like to do?
1. Visit an animal
2. Add an animal
3. Show stats
4. Exit
"""
    Z1 = Zoo("Johanessburg Zoo", 20)
    while True:
        choice = input(menu).strip()

        if choice == "1":
            print("Visiting an animal...")
            type = input("Enter the type of animal you wish to visit (Lion, Elephant, Snake): ").strip()

            if type == "Lion":
                Z1.visit_animal(type)
            elif type == "Elephant":
                Z1.visit_animal(type)
            elif type == "Snake":
                Z1.visit_animal(type)

        elif choice == "2":
            aType = input("Enter the type of animal (Lion, Elephant, Snake): ").strip()
            name = input("Enter the name of the animal: ").strip()
            age = int(input("Enter the age of the animal: ").strip())

            if aType == "Lion":
                number_claws = int(input("Enter the number of claws: ").strip())
                animalInfo = {"type": "Lion", "name": name, "age": age, "number_claws": number_claws}
                Z1.add_animal(animalInfo,False)

            if aType == "Elephant":
                tusk_length = float(input("Enter the tusk length in meters: ").strip())
                animalInfo = {"type": "Elephant", "name": name, "age": age, "tusk_length": tusk_length}
                Z1.add_animal(animalInfo, False)
                
            if aType == "Snake":
                venomPotency = input("Enter the venom potency: ").strip()
                animalInfo = {"type": "Snake", "name": name, "age": age, "venomPotency": venomPotency}
                Z1.add_animal(animalInfo, False)

        elif choice == "3":
            print("Showing stats...")
            Z1.show_stats()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()