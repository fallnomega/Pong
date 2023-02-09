import turtle
from turtle import Turtle

class Paddle:
    def __init__(self):
        self.paddle  = self.add_paddle()

    def add_paddle(self):
        new_paddle = turtle.Turtle()
        new_paddle.setheading(90)
        new_paddle.penup()
        new_paddle.goto(350,0)
        new_paddle.shapesize(stretch_wid=1,stretch_len=5)
        new_paddle.shape("square")
        new_paddle.color("white")
        return new_paddle

    def move_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(),new_y)

    def move_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)



