from score import Scoreboard
from food import Food 
from turtle import Screen
from snake import Snake
import time


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    score = Scoreboard()
    snake = Snake()
    food = Food()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        #detect collision with food 
        if snake.head.distance(food) < 15:
            food.refresh()
            score.update_score()
            snake.extend()

        #detect collision with wall 
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
            game_is_on = False 
            score.game_over()
        
        #detect collision with tail 
        for segment in snake.segments[1:]:
#            if segment == snake.segments[0]:
#                pass
#            if  snake.segments[0].position() == segment.position():
            if snake.head.position() == segment.position(): # COULD BE DONE AS >>> if snake.head.(segment) < 10: 
                game_is_on = False
                score.game_over()

    screen.exitonclick()