import time
from turtle import Screen
from player import Player
from car_manager import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
cars = Cars()

play = Player()
screen.listen()
screen.onkey(play.move_up, "Up")
scoreboard = Scoreboard()
game_is_on = True
Speed = 0.1

while game_is_on:
    time.sleep(Speed)
    screen.update()
    cars.create_car()
    cars.move_cars()

    for car in cars.all_car:
        if car.distance(play) < 20:
            scoreboard.game_over()
            game_is_on = False

    if play.finish_line():
        play.goto_start()
        scoreboard.increase_level()
        Speed -= -0.002

screen.exitonclick()

