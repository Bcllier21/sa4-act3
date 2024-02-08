number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

if guess == number:
    print("Congratulations! You guessed the right number.")
elif guess != number:
    while guess != "q" or guess != number:
        print(f"Sorry! That's not the correct number.")
        guess = input(f"You can guess again, or press 'q' to quit. ")
        if guess == str(number):
            print("Congratulations! You guessed the right number.")
            break
        elif guess == "q":
            print(f"The correct number was actually {number}.")
            break