password = input("Please enter your password: ").strip()
last_char = password[-1]
first_char = password[0]
print(f"Your Password hint: it starts with '{first_char}' and ends with '{last_char}'")