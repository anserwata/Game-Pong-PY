from turtle import Turtle


class GameBar(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 260)

    def set_points(self, tray_left, tray_right):
        self.clear()
        self.write(f"Player {tray_left.game_color}: {tray_left.score}  "
                   f"Player {tray_right.game_color}: {tray_right.score}",
                   align="center",
                   font=("Calibri", 15, "normal"))


class EndGameBar(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color('red')
        self.hideturtle()
        self.goto(0, 50)

    def end_game(self, tray):
        self.clear()
        self.write(f"Player {tray.game_color} won with {tray.score} points",
                   align="center",
                   font=("Calibri", 30, "italic"))