from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 0)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.shape("circle")
        self.color("white")
        self.speed(10)

    def ball_move(self):

        new_y = self.ycor() + 20
        new_x = self.xcor() + 20
        self.goto(new_x, new_y)
