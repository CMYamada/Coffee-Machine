import random
import turtle as t

timmy = t.Turtle()
timmy.shape("turtle")
t.colormode(255)

colorsList = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen"
]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    randColor = (r,g,b)
    return randColor

# Shape Drawer
def draw_shapes(maxN):
    for shape in range(3, maxN):
        timmy.color(random.choice(colorsList))
        turn = 360 / shape
        for sides in range(shape):
            timmy.forward(100)
            timmy.right(turn)

# Random walk
def random_walk():
    timmy.pensize(5)
    timmy.speed(10)
    directions = [90, 180, 270, 360]

    for _ in range(100):
        timmy.color(random_color())
        dir = random.choice(directions)
        timmy.right(dir)
        timmy.forward(25)

# spirograph
def draw_spirograph(gapSize):
    timmy.speed(0)
    for _ in range(int(360/gapSize)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gapSize)

draw_spirograph(5)
# random_walk()
# draw_shapes(11)



screen = t.Screen()
screen.exitonclick()