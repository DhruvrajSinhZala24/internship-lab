import random

def guess_the_number():
    print("🎮 Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempt(s).")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()