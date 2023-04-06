import turtle
from turtle import Turtle, Screen
import random


is_game_on = False
game_not_ended = True
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
number_of_players = screen.numinput(title="choose number of players", prompt="How many players do we have ?")
for i in range(int(number_of_players)):
    user_bet = screen.textinput(title="Make your bet", prompt="which Turtle will win the race? Enter a color")
    bet_amount = screen.numinput(title="How much is your Stake?", prompt="How much is your stake in $: ")

# print(user_bet)
y_positions = [-100, -65, -25, 10, 45, 85, 120]
all_turtle = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_game_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've Won! the {winner_color} Turtle Won the race and your profit is: {bet_amount * 2}")
            else:
                print(f"You've Lost! the {winner_color} Turtle Won the race")
                # no_more_game = screen.textinput(title="continue", prompt="any more players? ")
                # if no_more_game == "no":
                #     game_not_ended = False
        random_walk = random.randint(0, 10)
        turtle.forward(random_walk)


# tut = Turtle(shape="turtle")
# tut.penup()
# tut.color("orange")
# tut.goto(x=-230, y=-65)
#
#
# chim = Turtle(shape="turtle")
# chim.penup()
# chim.color("yellow")
# chim.goto(x=-230, y=-25)
#
# bing = Turtle(shape="turtle")
# bing.penup()
# bing.color("green")
# bing.goto(x=-230, y=10)
#
# fing = Turtle(shape="turtle")
# fing.penup()
# fing.color("blue")
# fing.goto(x=-230, y=45)
#
# rand = Turtle(shape="turtle")
# rand.color("purple")
# rand.penup()
# rand.goto(x=-230, y=85)


screen.exitonclick()