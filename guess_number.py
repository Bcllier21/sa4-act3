number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

if guess == number:
    print("Congratulations! You guessed the right number.")
elif guess != number:
    counter = 7        
    print(f"Sorry! That's not the correct number. You get {counter} more guesses.")
    while guess != "q" or guess != number:
        guess = input(f"You can guess again, or press 'q' to quit. ")
        if guess == str(number):
            print("Congratulations! You guessed the right number.")
            break
        elif guess != str(number) and counter == 2:
            counter -= 1
            print(f"Sorry! You have {counter} guess remaining before the answer's shown.")
        elif guess != str(number) and counter > 1:
            counter -= 1
            print(f"Sorry! You have {counter} guesses remaining before the answer's shown.")
        elif guess == "q" or counter == 1:
            print(f"The correct number was actually {number}.")
            break