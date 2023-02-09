import turtle
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self = self.add_paddle(x_pos)

    def add_paddle(self, x_position):
        self.setheading(90)
        self.penup()
        self.goto(x_position, 0)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.shape("square")
        self.color("white")
        return self

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
