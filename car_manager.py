from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def color_selector():
    n = random.randint(0, len(COLORS) - 1)
    return COLORS[n]


def random_position():
    y_cor = random.randint(-250, 250)
    x_cor = random.randint(0, 200)
    random_pos = (x_cor, y_cor)
    return random_pos


class CarManager:
    def __init__(self):
        self.cars = []
        self.generate()
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(color_selector())
        new_car.penup()
        new_car.goto(random_position())
        self.cars.append(new_car)

    def generate(self):
        for _ in range(1, 10):
            self.create_car()

    def move(self):
        for cars in self.cars:
            cars.backward(self.speed)

    def new_car(self):
        self.create_car()
        self.cars[-1].goto(300, random_position()[1])

    def level_up(self):
        self.speed += 5


