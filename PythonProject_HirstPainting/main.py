# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.png',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
# (251, 246, 239), (251, 245, 248) bgcolors removed from color_list

color_list = [(234, 243, 249), (237, 248, 243), (228, 153, 70), (235, 215, 89), (48, 107, 146), (110, 176, 205), (162, 55, 74), (213, 135, 149), (215, 62, 89), (161, 81, 40), (134, 31, 61), (189, 158, 23), (230, 76, 43), (125, 197, 161), (237, 165, 189), (52, 180, 106), (143, 226, 194), (62, 46, 59), (142, 37, 27), (89, 118, 186), (136, 211, 226), (63, 124, 82), (47, 37, 62), (51, 171, 187), (33, 82, 75), (234, 170, 162), (196, 221, 11), (171, 190, 219)]
import random
import turtle
turtle.colormode(255)
t = turtle.Turtle()
t.color("white")

screen = turtle.Screen()
screen.bgcolor("lightgray")
t.speed(0)
t.penup()
t.setheading(225)
t.fd(300)
t.setheading(0)
for col in range(10):
    for row in range(10):
        t.dot(20,random.choice(color_list))
        t.fd(50)
    t.setheading(90)
    t.fd(50)
    t.setheading(180)
    t.fd(500)
    t.setheading(0)
t.hideturtle()

screen.exitonclick()