import time
import turtle

from components.ball import Ball
from components.game_bar import GameBar, EndGameBar
from components.tray import Tray

# points to win
max_points = 10

game_window = turtle.Screen()
game_window.title('PONG GAME')
game_window.bgcolor(0, 0, 0)
game_window.setup(width=800, height=600)
game_window.tracer(0)

# tray
tray_left = Tray('yellow', -350)
tray_right = Tray('blue', 350)

# ball
ball = Ball()

# status bar
bar = GameBar()

# keyboard moves tracking
game_window.listen()
game_window.onkeypress(tray_left.move_up, 'w')
game_window.onkeypress(tray_left.move_down, 's')
game_window.onkeypress(tray_right.move_up, 'Up')
game_window.onkeypress(tray_right.move_down, 'Down')

# main loop
while True:
    game_window.update()

    bar.set_points(tray_left, tray_right)

    ball.move()
    ball.bounce_tray(tray_left, tray_right)
    ball.bounce_window(tray_left, tray_right)

    if tray_left.score == max_points or tray_right.score == max_points:
        time.sleep(1)
        ball.goto(0, 0)

        if tray_left.score > tray_right.score:
            EndGameBar().end_game(tray_left)
        else:
            EndGameBar().end_game(tray_right)

