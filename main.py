from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time
from scoreboard import ScoreBoard



s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("La viborita")
s.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:

    s.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.raise_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.high_score()

        score.reset_score()
        snake.reset()


    for elem in snake.list[1:]:

        if snake.head.distance(elem) < 10:
            score.high_score()
            score.reset_score()
            snake.reset()

s.exitonclick()