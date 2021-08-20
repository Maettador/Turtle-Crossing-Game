import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
cars = []
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up, "Up")

for i in range(10):
    cars.append(CarManager())

turns = 0

game_is_on = True
while game_is_on:
    turns += 1
    time.sleep(0.1)
    screen.update()
    scoreboard.display_level()
    if turns % 6 == 0:
        cars.append(CarManager())
    for car in cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
        if car.xcor() <= -280:
            car.start()
        car.car_move()
        if player.ycor() >= 280:
            player.start()
            car.speed_up()
            scoreboard.next_level()



screen.exitonclick()
