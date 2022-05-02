import time
from turtle import Screen
from player import Player
from car import Car
from level import Level

game_on = True

# screen stuff
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# initializing objects
player = Player()
car = Car()
level = Level()

# player movements
screen.onkey(player.up, "Up")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")
screen.onkey(player.go_down, "Down")

while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    if player.is_at_finish_line():
        level.next_level()
        player.reset_player()
        car.level_up()

    for cur_car in car.cars[0:]:
        if player.distance(cur_car) < 20:
            level.game_over()
            game_on = False

screen.exitonclick()
