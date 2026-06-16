from art import logo, vs
from game_data import data
import random

def formatData(item):
    acc_name = item["name"]
    acc_desc = item["description"]
    acc_country = item["country"]
    return f"{acc_name}, a {acc_desc}, from {acc_country}"

def checkAnswer(guess, aFollowers, bFollowers):
    if aFollowers > bFollowers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
higherLower = True
B = random.choice(data)

while higherLower:
    A = B
    B = random.choice(data)
    if B == A:
        B = random.choice(data)
    print(f"Compare A: {formatData(A)}.")
    print(vs)
    print(f"Against B: {formatData(B)}.")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n"*20)
    a_followers = A["follower_count"]
    b_followers = B["follower_count"]
    isCorrect = checkAnswer(choice, a_followers, b_followers)

    if isCorrect:
        score += 1
        print(f"You're correct! Current Score: {score}.")
    else:
        print(f"That's wrong! The score is {score}.")
        score = 0
        higherLower = False