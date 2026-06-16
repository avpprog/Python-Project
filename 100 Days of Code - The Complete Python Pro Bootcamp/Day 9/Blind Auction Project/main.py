# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)

bid_record = {}
print("Welcome to Secret Auction Program")

continue_bidding = True
while continue_bidding:
    name = input("What is your name? => ")
    bid = int(input("What is your bid? => $ "))
    bid_record[name] = bid
    choice = input("Continue auction? (y/n) => ").lower()
    print("\n"*50)
    if choice == "y":
        continue_bidding = True
    else:
        continue_bidding = False

winner = ""
bid_winner_amt = 0
for bidder in bid_record:
    bid_amt = bid_record[bidder]
    if bid_amt > bid_winner_amt:
        bid_winner_amt = bid_amt
        winner = bidder

print(logo)
print(f"{winner} wins the auction with bid of ${bid_winner_amt}")

