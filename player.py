from turtle import Turtle
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.left(90)
        self.shape("turtle")
        self.penup()
        self.go_to_start()


    def move(self):
        self.fd(MOVE_DISTANCE)

    def check_win(self):
        return self.ycor() >= FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)