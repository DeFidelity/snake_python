from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
game_is_on = True

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "x")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.animate_snake()
    # Detect collision with wall
    if snake.head.distance(food) < 15:
        food.food_location()
        scoreboard.increase_score()
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        scoreboard.reset()
        snake.reset()
    elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    # Detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
