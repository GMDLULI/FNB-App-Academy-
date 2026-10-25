#Simple countdown using while loop 
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blast off")

# simple rep Counter using for loop

for rep in range(1, 4):
    print(f'This is rep no.{rep}')

# creating a guessing game 
secret_word = "python"


while True:
    guess = input("Guess the programming language we are using: ").lower()
    if guess == secret_word:
        print("You guessed it right! Congratulations!")
        break
    else:
        print("Incorrect guess. Try again.")




