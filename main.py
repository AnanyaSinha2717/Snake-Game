from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Feed the Snake')
screen.tracer(0)

# screen boundary
bound = Turtle()
bound.ht()
bound.pensize(20)
bound.pu()
bound.color('silver')
bound.goto(-280, 280)
bound.pd()
for j in range(4):
  bound.fd(560)
  bound.right(90)

# calling classes
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  # detect collision with food
  if snake.snake[0].distance(food) < 18:
    food.refresh()
    snake.extend()
    score.score_calc()

  # detect collision with wall
  if snake.snake[0].xcor() > 270 or snake.snake[0].xcor(
  ) < -270 or snake.snake[0].ycor() > 270 or snake.snake[0].ycor() < -270:
    score.reset_board()
    snake.reset_snake()

  # detect collision with tail
  for seg in snake.snake[1:]:
    if seg == snake.snake[0]:
      pass
    elif snake.snake[0].distance(seg) < 10:
      score.reset_board()
      snake.reset_snake()

screen.exitonclick()
