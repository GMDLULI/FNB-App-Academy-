# Defining a function
def greet_user():
    print("Welcome to the Application!")

#Calling the function
greet_user()

# Defining a function with parameters
def vat_calculator(amount):
    tax = amount * 0.15
    print(f"The VAT for the amount R{amount} is: R{round(tax, 2)}")

vat_calculator(100)
vat_calculator(200)