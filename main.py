import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
game_speed = 0.1
counter = 0
screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.bgcolor("white")
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(game_speed)
    screen.update()
    screen.onkey(player.move, "Up")
    screen.listen()
    car_manager.spawn()
    car_manager.move_cars()

    #detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #check if player crossed to the other side
    if player.check_win():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()