import turtle
from turtle import Turtle

class Paddle:
    def __init__(self):
        paddle  = self.add_paddle()

    def add_paddle(self):
        new_paddle = turtle.Turtle()
        new_paddle.setheading(90)
        new_paddle.setx(350)
        new_paddle.shapesize(stretch_wid=1,stretch_len=5)
        new_paddle.shape("square")
        new_paddle.color("white")


