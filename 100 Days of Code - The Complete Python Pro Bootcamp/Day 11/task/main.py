from art import logo
import random
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
dealer = []

def deal_card(hand):
    hand.append(random.choice(cards))

def starting_hand():
    for _ in range(2):
        deal_card(player)
        deal_card(dealer)

def calculate(hand):
    total = 0
    for card in hand:
        total += card
    return total

def status(hand):
    print(f"Your cards: {hand}, Current score: {calculate(hand)}")
    print(f"Dealer's first card: {dealer[0]}")


def playGame():
    play = input("Do you want to play a game of Blackjack? (y/n): ")
    if play == "y" or play == "Y":
        playing = True
        while playing:
            starting_hand()
            status(player)
            if calculate(player) == 21:
                print("You win!")
                break
            if calculate(dealer) == 21:
                print("You lose!")
                break

            getcard = input("Type 'y' to get another card, 'n' to pass: ")
            if getcard == "y":
                deal_card(player)
                status(player)
                if calculate(player) > 21:
                    print("You lose!")
                    break

            else:
                status(player)
                while calculate(dealer) < 17:
                    deal_card(dealer)
            playing = False
        playGame()
    else:
        return
playGame()