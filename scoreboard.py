from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.current_level = 1
        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def next_level(self):
        self.current_level += 1

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
