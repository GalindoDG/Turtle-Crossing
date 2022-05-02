from turtle import Turtle
ALIGN = "center"
FONT = (["Courier", 25, "normal"])


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.current_level = 1
        self.color("black")
        self.goto(-230, 260)
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.current_level}",
                   move=False,
                   align=ALIGN,
                   font=FONT)

    def next_level(self):
        self.current_level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER",
                   move=False,
                   align=ALIGN,
                   font=FONT)