from turtle import Turtle, Screen

def move_forward():
    korni.forward(10)

if __name__ == '__main__':
    korni = Turtle()
    my_screen = Screen()
    my_screen.listen() 
    my_screen.onkey(fun=move_forward, key="space")
    my_screen.exitonclick()