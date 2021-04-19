from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def moveForward():
    tim.forward(10)


def moveBackward():
    tim.backward(10)


def turnRight():
    tim.right(10)


def turnLeft():
    tim.left(10)


def clearScreen():
    screen.reset()


screen.listen()
screen.onkey(key="w", fun=moveForward)
screen.onkey(key="s", fun=moveBackward)
screen.onkey(key="a", fun=turnLeft)
screen.onkey(key="d", fun=turnRight)
screen.onkey(key="c", fun=clearScreen)
screen.exitonclick()
