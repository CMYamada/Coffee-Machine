
import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
t.colormode(255)
colors = [(237, 237, 241), (26, 109, 164), (194, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (222, 137, 176), (143, 109, 57), (101, 197, 219), (206, 166, 29), (21, 58, 132), (212, 75, 91), (238, 89, 49), (141, 208, 227), (119, 192, 141), (6, 160, 87), (4, 186, 179), (106, 108, 198), (136, 29, 72), (98, 51, 37), (25, 153, 211), (228, 168, 188), (153, 213, 195), (173, 186, 221), (234, 174, 162), (30, 91, 95), (87, 47, 34), (34, 46, 84)]

screen = t.Screen()
screen.bgcolor('black')
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for up in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(colors))
        timmy.forward(50)
    if up % 2 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
    else:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(0)


screen.exitonclick()
