# classes in pong
# paddles/slider
# individual player score
# ball
import time
import turtle
import paddle
import ball
import ball
from turtle import Screen

# TODO list

# 4 Create the ball and make it move
# 5 Detect collision with wall and bounce
# 6 Detect collision with paddle
# 7 Detect when paddle misses
# 8 Keep Score

screen = turtle.Screen()
screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

player1 = paddle.Paddle(-350)
player2 = paddle.Paddle(350)
ball = ball.Ball()
screen.onkey(player1.move_up, "Up")
screen.onkey(player1.move_down, "Down")

screen.onkey(player2.move_up, "w")
screen.onkey(player2.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    # time.sleep(.1)
    ball.ball_move()

screen.exitonclick()
