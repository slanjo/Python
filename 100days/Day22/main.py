from scoreboard import Scoreboard
from ball import Ball
from turtle import Screen
from paddle import Paddle
import time

if __name__ == '__main__':
    screen = Screen()
    screen.setup(800, 600)
    screen.title("Ping-Pong Game")
    screen.bgcolor("black")
    screen.tracer(0)

    l_paddle = Paddle((-360, 0))
    r_paddle = Paddle((350, 0)) 
    ball = Ball()    
    score = Scoreboard()
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    game_on = True
    sleep_time = 0.1 #my ugly solution for speed reset to default upon a miss 

    while game_on:
#        time.sleep(sleep_time)  #my ugly solution for speed reset to default upon a miss 
        time.sleep(ball.sleep_time)
        screen.update()
        print(ball.sleep_time)
        ball.move()

    #detect collision with the wall
        if ball.ycor() > 280 or ball.ycor() < -280: 
            ball.bounce_y()
    
    #detect collision with the paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
            ball.bounce_x() 
#            sleep_time *= .9 #speed up the ball every time it hits the paddle  #my ugly solution for speed reset to default upon a miss 
            

    #detect r_paddle ball out of bounds
        if ball.xcor() > 380: 
            ball.reset_position()
            score.update_score(1)
#            sleep_time = 0.1   #my ugly solution for speed reset to default upon a miss 

    #detect l_paddle ball out of bounds
        if ball.xcor() < -390:
            ball.reset_position()
            score.update_score(2)
#            sleep_time = 0.1   #my ugly ugly solution for speed reset to default upon a miss 