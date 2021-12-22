from turtle import Turtle, Screen

def mv_fd():
    korni.fd(10)
def mv_bck():
    korni.back(10)
def mv_clck():
    korni.setheading(korni.heading() + 10) 
def mv_cnt_clck():
    korni.setheading(korni.heading() - 10) 
def clr_scrn():
#    my_screen.clearscreen()
    korni.clear()
    korni.penup()
    korni.home()
    kornin.pendown()
    
if __name__ == '__main__':
    korni = Turtle()
    my_screen = Screen()
    my_screen.listen() 

    my_screen.onkey(fun=mv_fd, key="w")
    my_screen.onkey(fun=mv_fd, key="w")
    my_screen.onkey(fun=mv_bck, key="s")
    my_screen.onkey(fun=mv_cnt_clck, key="a")
    my_screen.onkey(fun=mv_clck, key="d")
    my_screen.onkey(fun=clr_scrn, key="c")

    my_screen.exitonclick()