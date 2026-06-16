import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player:
    def __init__(self):
        self.turtle = Turtle("turtle")
        self.turtle.penup()
        self.turtle.goto(STARTING_POSITION)
        self.turtle.setheading(90)

    def up(self):
        self.turtle.fd(MOVE_DISTANCE)

    def down(self):
        self.turtle.bk(MOVE_DISTANCE)




