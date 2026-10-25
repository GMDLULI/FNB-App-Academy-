while True:
    score = input("Enter your score: ").strip().lower()
    if score == "stop":
        print('Game Ended!!')
        break
    elif score.isdigit():
        score = int(score)
        if score > 100:
            print("Wow! Thats a new high score!")
            break
        else:
            print("Good Try, keep playing!")
            break
    else:
        print("Invalid input. Please enter a valid score or type 'stop' to end the game.")


