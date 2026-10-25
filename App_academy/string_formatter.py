first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio about yourself: ").strip()

user_name = f"{first_name[0]}{last_name}".lower()
full_name = f"{first_name.title()} {last_name.title()}"
number_of_characters = len(bio)
intro = bio.replace("I am", "I'm")

print (f"Hello, {full_name}! Your bio has {number_of_characters} characters.")
print(f"Your username is: {user_name}")
print(f"Intro: {intro}")
