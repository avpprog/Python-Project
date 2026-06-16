# from turtle import Turtle, Screen
#
# tim = Turtle()
# print(tim)
# tim.shape("turtle")
# tim.color("DarkOrchid")
# tim.fd(100)
#
# myscreen = Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)
