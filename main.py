from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coord = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240, y_coord[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:

        if turtles.xcor() > 230:
            winning_turtle = turtles.pencolor()
            is_race_on = False
        random_distance = random.randint(0,10)
        turtles.forward(random_distance)

if winning_turtle == user_bet:
    print("You won the bet, turtle master!")
else:
    print(f"Sorry. The {winning_turtle} turtle is the winning turtle. LOSER")
screen.exitonclick()
