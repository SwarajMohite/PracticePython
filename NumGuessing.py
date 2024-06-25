import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Try to guess it!")

guess = None  # Initialize guess to None

# Loop until the user guesses the correct number
while guess != number_to_guess:
    # Increment the number of attempts
    attempts += 1

    # Get the user's guess
    guess = int(input("Enter your guess: "))
    
    # Check if the guess is too high, too low, or correct
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")

# If the guess is correct, congratulate the user
print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")