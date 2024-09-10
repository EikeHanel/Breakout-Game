from turtle import Turtle
import random
X_DIRECTION = random.choice([10, -10])
Y_DIRECTION = -10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = X_DIRECTION
        self.y_move = Y_DIRECTION
        self.move_speed = 0.075

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.075

    def increase_speed(self):
        self.move_speed *= 0.9  # Increase speed by 10%

    def check_collision(self, ball, blocks):
        for block in blocks:
            if ball.distance(block) < 40:  # Approximate collision distance (adjust if needed)
                block.hideturtle()  # Hide the block on collision
                blocks.remove(block)  # Remove the block from the list
                self.bounce_y()  # Reverse the ball's direction
                self.increase_speed()
                break
