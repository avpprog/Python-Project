from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("blue", "pink")
screen = Screen()
screen.bgcolor("black")

# Square
# n = 4
# while n > 0:
#     tim.forward(100)
#     tim.left(90)
#     n -= 1

# Dashed line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Shapes
# def draw_shape(sides):
#     angle = 360 / i
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
# col = ["red", "orange", "yellow", "green", "blue", "violet", "purple","black"]
# for i in range(3,11):
#     tim.color(col[i-3])
#     draw_shape(i)

# Random Walk
# import random
# tim.pensize(5)
# colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]
# angle = [0, 90, 180, 270]
# tim.hideturtle()
# tim.speed(0)
# for i in range(300):
#     tim.color(random.choice(colors),"black")
#     tim.forward(30)
#     tim.setheading(random.choice(angle))

# Spirograph
tim.speed("fastest")
tim.hideturtle()
tim.pensize(3)
colors = ["violet", "lightblue", "lightgreen"]
for i in range(30):
    tim.pencolor(colors[i%3])
    tim.circle(100)
    tim.right(12)

screen.exitonclick()