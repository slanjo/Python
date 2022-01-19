from turtle import Screen
from snake import Snake
import time


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
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
#   korni_1 = Turtle(shape="square") 
#   korni_1.color("white", "white") 
#   korni_2 = Turtle(shape="square") 
#   korni_2.color("white", "white") 
#   korni_2.setposition(korni_1.xcor() - 20, 0.0)
#   korni_3 = Turtle(shape="square") 
#   korni_3.color("white", "white") 
#   korni_3.setposition(korni_2.xcor() - 20, 0.0)


    screen.exitonclick()