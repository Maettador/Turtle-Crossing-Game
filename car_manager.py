from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.turtlesize(stretch_len=2)
        self.setheading(180)
        self.start()
        self.velocity = STARTING_MOVE_DISTANCE

    def car_move(self):
        self.forward(self.velocity)

    def start(self):
        self.goto(260, random.randint(-250, 250))

    def speed_up(self):
        self.velocity += MOVE_INCREMENT


