from turtle import Turtle, Screen
import random

isRaceOn = False
screen = Screen()
screen.setup(width=500, height=400)
userBet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
coordinates = [-70, -40, -10, 20, 50, 80]
allTurtles = []
for turtle_index in range(0, 6):
    newTurtle = Turtle(shape='turtle')
    newTurtle.color(colors[turtle_index])
    newTurtle.penup()
    newTurtle.goto(x=-225, y=coordinates[turtle_index])
    allTurtles.append(newTurtle)

if userBet:
    isRaceOn = True

while isRaceOn:

    for turtle in allTurtles:
        if turtle.xcor() > 230:
            isRaceOn = False
            winner = turtle.pencolor()
            if winner == userBet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        randDistance = random.randint(0, 10)
        turtle.forward(randDistance)


screen.exitonclick()