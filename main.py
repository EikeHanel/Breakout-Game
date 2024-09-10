from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from block import create_blocks_uniform
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.title("Breakout")
screen.tracer(0)


paddle = Paddle((0, -380))
ball = Ball()
blocks = create_blocks_uniform(num_blocks_per_row=6, num_rows=4)

win_turtle = Turtle()
win_turtle.hideturtle()
win_turtle.color("white")
win_turtle.penup()
win_turtle.goto(0, 0)

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

game_over = False
life = 3
while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.check_collision(ball, blocks)

    # detect collision with wall
    if ball.xcor() >= 280 or ball.xcor() <= -280:
        ball.bounce_x()

    if ball.ycor() >= 380:
        ball.bounce_y()

    # collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() <= -370:
        ball.bounce_y()

    # out of bounce
    if ball.ycor() < -400:
        life -= 1
        ball.reset_position()
        screen.update()
        if life == 0:
            screen.update()
            game_over = True
            win_turtle.hideturtle()
            win_turtle.write("You Lose!", align="center", font=("Arial", 24, "bold"))
        time.sleep(1)

    if not blocks:
        screen.update()
        game_over = True
        win_turtle.hideturtle()
        win_turtle.write("You Win!", align="center", font=("Arial", 24, "bold"))

screen.exitonclick()
