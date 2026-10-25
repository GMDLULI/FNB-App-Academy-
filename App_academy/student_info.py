name = input("Enter your Name: ")
lastName = input("Enter your Last Name: ")
age = int(input("Enter your Age: "))
favoriteNumber = float(input("Enter your Favorite Number: "))

print(f"Welcome {name.upper()}")
print(f"Welcome {name.title()} {lastName.title()}")

month = age * 12
print(f"You are {month} months old.")

print (f"Your favorite number is {round(favoriteNumber, 2)}.")

print(f"Variable Types: Name: {type(name)} Last Name: {type(lastName)} Age: {type(age)} Favorite Number: {type(favoriteNumber)}")
