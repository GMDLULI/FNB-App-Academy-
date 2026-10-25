# Drag individual letters 
name = "Python"
print(name[0])
print(name[-1])
print(name[2:5])

#using String methods

town = "  Johannesburg  "
print(town.upper())
print(town.strip()) # removes whitespace from the beginning and end of the string

# Build an email generator

firstName = input("Enter your first name: ").strip()
lastName = input("Enter your last name: ").strip()
userName = f"{firstName[0]}{lastName}"
print(f"Your email address is: {userName.lower()}023@WeThinkCode.co.za")