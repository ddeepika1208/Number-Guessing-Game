import random

print("🎮 Welcome to the Number Guessing Game!")

while True:
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Correct! You guessed it in "f"{attempts} attempts!")
                break

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if play_again != "yes":
        print("Thanks for playing! 😊")
        break