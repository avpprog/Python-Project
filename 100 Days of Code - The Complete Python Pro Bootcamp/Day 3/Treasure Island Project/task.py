print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
junction = input("You want to go 'left' or 'right': ").lower()
if junction == "left":
    water = input("Will you 'wait' for the boat or 'swim' across the lake: ").lower()
    if water == "wait":
        door = input("Which door would you like to enter 'Red', 'Blue' or 'Yellow': ").lower()
        if door == "yellow":
            print("Congratulations! You won the treasure!")
        elif door == "red":
            print("You fell into the lava pool and died.\nGAME OVER!")
        elif door == "blue":
            print("You encountered beasts and died fighting.\nGAME OVER!")
        else:
            print("You were teleported out of 'The Treasure Island'\nGAME OVER!")
    else:
        print("You were poisoned by jelly fish and died.\nGAME OVER!")
elif junction == "right":
    print("You fell into a pit.\nGAME OVER!")
else:
    print("Wrong input. Game Over!")



