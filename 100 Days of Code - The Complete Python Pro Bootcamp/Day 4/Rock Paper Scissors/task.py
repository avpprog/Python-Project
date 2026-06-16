rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
moves = [rock, paper, scissors]
computer_move = random.choice(moves)
playerChoice = int(input("What is your move?\n0 for rock, 1 for paper, 2 for scissors"))
player_move = moves[playerChoice]
print("Your move:",player_move)
print("Computer's move:",computer_move)

if computer_move == "rock" and player_move == "paper":
        print("You win")
elif computer_move == "rock" and player_move == "scissors":
    print("You lose")
elif computer_move == "paper" and player_move == "scissors":
    print("You win")
elif computer_move == "paper" and player_move == "rock":
    print("You lose")
elif computer_move == "scissors" and player_move == "rock":
    print("You win")
elif computer_move == "scissors" and player_move == "paper":
    print("You lose")
else:
    print("Game Over")
