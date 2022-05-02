from turtle import Turtle

MOVE = 10
STARTING_POS = (0, -280)
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.speed("fastest")
        self.color("green")
        self.seth(90)
        self.goto(STARTING_POS)

    def up(self):
        self.seth(90)
        self.forward(MOVE)

    def go_left(self):
        self.seth(180)
        self.forward(MOVE)

    def go_right(self):
        self.seth(0)
        self.forward(MOVE)

    def go_down(self):
        self.seth(270)
        self.forward(MOVE)

    def reset_player(self):
        self.goto(STARTING_POS)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
