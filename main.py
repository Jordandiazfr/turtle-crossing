import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
cars = CarManager()

# Event keys
screen.listen()
screen.onkey(fun=player.move, key="Up")

# Game on
game_is_on = True
counter = 6

while game_is_on:
    counter += 1
    time.sleep(0.1)
    screen.update()
    # Generate cars every 6th time the  loop runs
    if counter % 6 == 0:
        cars.new_car()
    # Move the cars to the left
    cars.move()

    # Detect collision with the car
    for car in cars.cars:
        if player.distance(car) < 25:
            print("yay")
            score.game_over()
            game_is_on = False

    # Detect if the  player leveled up
    if player.ycor() > 280:
        player.next_level()
        score.next_level()
        cars.level_up()
        time.sleep(0.5)

screen.exitonclick()
