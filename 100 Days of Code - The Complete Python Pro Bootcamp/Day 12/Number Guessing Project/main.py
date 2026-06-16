from art import logo
import random
print(logo)
print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)
print(random_number)
difficulty = input("Choose a difficulty. \n Type 'easy' or 'hard':\t").lower()
attempts = 0
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > random_number:
        print("You guessed too high.")
    elif guess < random_number:
        print("You guessed too low.")
    elif guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        break
    attempts -= 1
    if attempts == 0:
        print(f"You've run out of guesses.")