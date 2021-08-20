from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.start()

    def start(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.l_new = self.xcor() - MOVE_DISTANCE
        self.goto(self.l_new, self.ycor())

    def move_right(self):
        self.r_new = self.xcor() + MOVE_DISTANCE
        self.goto(self.r_new, self.ycor())

