from turtle import Turtle


class Tray(Turtle):

    def __init__(self, color, dim):
        super().__init__()
        self.speed(0)
        self.shape('square')
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(dim, 0)
        self.game_color = color.upper()
        self.score = 0

    def move_up(self):
        y = self.ycor()
        y += 20

        if y <= 260:
            self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20

        if y >= -250:
            self.sety(y)

