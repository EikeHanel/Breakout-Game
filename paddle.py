from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(position)

    def move_left(self):
        new_x = self.xcor() - 25
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 25
        self.goto(new_x, self.ycor())
