from turtle import Turtle
import random

COLORS = ["blue", "brown", "red", "orange", "purple", "black", "pink", "purple", "indigo"]
MOVE_INCREMENT = 2
STARTING_MOVE_DIST = 5
NUM_OF_CARS = 15


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.cars = []
        self.car_speed = STARTING_MOVE_DIST

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.pu()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            rand_y = random.randint(-250, 250)
            new_car.goto(300, rand_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
