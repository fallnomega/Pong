# classes in pong
# paddles/slider
# individual player score
# ball
import time
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
screen.tracer(0)
screen.listen()


player = paddle.Paddle()
screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down,"Down")



game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()
