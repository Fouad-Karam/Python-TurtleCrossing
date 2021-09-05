from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("TurtleCrossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
new_car = Cars()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.03)
    screen.update()

    new_car.create_car()
    new_car.move_cars()

    # Detect collision with cars
    for car in new_car.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect that turtle crossed the road
    if player.ycor() > 260:
        player.reset_position()
        new_car.level_up()
        scoreboard.increase_score()

screen.exitonclick()
