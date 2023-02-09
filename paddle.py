import turtle
from turtle import Turtle

class Paddle:
    def __init__(self):
        self.paddle  = self.add_paddle()

    def add_paddle(self):
        new_paddle = turtle.Turtle()
        new_paddle.setheading(90)
        new_paddle.goto(350,0)
        new_paddle.shapesize(stretch_wid=1,stretch_len=5)
        new_paddle.shape("square")
        new_paddle.color("white")
        new_paddle.penup()
        return new_paddle

    def move_up(self):
        self.paddle.forward(20)

    def move_down(self):
        self.paddle.backward(20)




