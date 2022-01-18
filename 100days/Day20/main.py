from turtle import Turtle, Screen



if __name__ == '__main__':
    kornjaca = Turtle(shape="square") 
    kornjaca.shape("square")
    kornjaca.color("white", "white") 
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")








screen.exitonclick()