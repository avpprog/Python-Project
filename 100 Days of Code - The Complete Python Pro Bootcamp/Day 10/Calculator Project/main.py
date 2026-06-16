def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 // n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

from art import logo
# print(operations["*"](4,8))
def calc():
    print(logo)
    continueCal = True
    num1 = int(input("Enter first number: "))
    while continueCal:
        opr = input("Choose operation: \n\t+\n\t-\n\t*\n\t/\nChoice: ")
        oper = operations[opr]
        num2 = int(input("Enter second number: "))
        res = oper(num1, num2)
        print(f"{num1} {opr} {num2} = {res}")
        cont = input("Do you want to continue (y/n): ")
        if cont == "y":
            continueCal = True
            num1 = res
        elif cont == "n":
            continueCal = False
            print("\n"*20)
            calc()
        else:
            print("Invalid option")
    return

calc()