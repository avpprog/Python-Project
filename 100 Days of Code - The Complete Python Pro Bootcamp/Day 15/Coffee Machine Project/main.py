MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report(resource):
    return f"Water: {resources['water']} ml \nMilk: {resources['milk']} ml \nCoffee: {resources['coffee']} g \nAmount: ${amount}"

amount = 0.00
print("hello")
choice = input("What would you like? (espresso/latte/cappuccino):").lower()
if choice == "espresso":
    print("espresso")
elif choice == "latte":
    print("latte")
elif choice == "cappuccino":
    print("cappuccino")
elif choice == "report":
    rep = report(resources)
    print(rep)
else:
    print("off")