import turtle
t = turtle.Turtle()
scr = turtle.Screen()
t.setheading(90)

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

scr.listen()
scr.onkey(move_forward, "w")
scr.onkey(move_backward, "s")
scr.onkey(turn_left, "a")
scr.onkey(turn_right, "d")
scr.onkey(clear_screen, "c")















scr.exitonclick()