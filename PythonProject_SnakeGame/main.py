import time
from turtle import  Screen
from food import Food
from snake import Snake
from scroreboard import ScoreBoard


scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

scr.listen()
scr.onkey(snake.up,"Up")
scr.onkey(snake.down,"Down")
scr.onkey(snake.left,"Left")
scr.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    #Detecting food collision
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend_segment()
        score.increase_score()

    #Detecting collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        score.game_over()

    #Detecting collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            score.game_over()


scr.exitonclick()