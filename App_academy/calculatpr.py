num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))


try:
    print(f"Addition: {num1 + num2:.2f} ")
    print(f"Subtraction: {num1 - num2:.2f} ")
    print(f"Multiplication: {num1 * num2:.2f} ")
    print(f"Division: {num1 / num2:.2f} ")
    print(f"Floor Division: {num1 // num2:.2f} ")
    print(f"Modulus: {num1 % num2:.2f} ")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")    


