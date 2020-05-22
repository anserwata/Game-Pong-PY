from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.dx = 0.3
        self.dy = 0.3

    def change_dir(self):
        self.dx *= -1

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_window(self, tray_left, tray_right):
        # top border
        if self.ycor() > 290 or self.ycor() < -290:
            self.dy *= -1

        # right edge, player score
        if self.xcor() > 390:
            self.goto(0, 0)
            self.dx *= -1
            tray_left.score += 1

        # left edge, player score
        if self.xcor() < -390:
            self.goto(0, 0)
            self.dx *= -1
            tray_right.score += 1

    def bounce_tray(self, tray_left, tray_right):
        if 340 < self.xcor() < 350 and tray_right.ycor() - 50 < self.ycor() < tray_right.ycor() + 50:
            self.dx *= -1

        if -350 < self.xcor() < -340 and tray_left.ycor() - 50 < self.ycor() < tray_left.ycor() + 50:
            self.dx *= -1
