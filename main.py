# classes in pong
# paddles/slider
# individual player score
# ball
import turtle
import paddle
from turtle import Screen

# TODO list
# 2 Crate and move the paddle
# 3 Create another paddle
# 4 Create the ball and make it move
# 5 Detect collision with wall and bounce
# 6 Detect collision with paddle
# 7 Detect when paddle misses
# 8 Keep Score

screen = turtle.Screen()
screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.title("Pong")

player1 = paddle.Paddle()

screen.exitonclick()
