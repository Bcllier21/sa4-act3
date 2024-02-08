number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

if guess == number:
    print("Congratulations! You guessed the right number.")
elif guess != number:
    print(f"Sorry! That's not the correct number.")
    if guess < number: print("Too low of a guess.")
    elif guess > number: print("Too high of a guess.")
    while guess != "q" or guess != number:
        guess = input(f"You can guess again, or press 'q' to quit. ")
        if guess == str(number):
            print("Congratulations! You guessed the right number.")
            break
        elif guess != str(number):
            if int(guess) < number: print("Too low of a guess.")
            elif int(guess) > number: print("Too high of a guess.")
        elif guess == "q":
            print(f"The correct number was actually {number}.")
            break