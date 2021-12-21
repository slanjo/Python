#import colorgram 
##### Draw a spot painting using colors extracted by colorgram from one of the Hirsts JPEGs #####
import turtle as t
import random

if __name__ == '__main__':
    pallette =  [(235, 242, 249), (237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34), (71, 10, 28), (10, 98, 50), (166, 181, 232), (237, 170, 159), (253, 5, 42), (9, 87, 103), (21, 35, 249), (63, 100, 8), (253, 9, 5), (0, 246, 244), (0, 250, 254)]
#    colors = colorgram.extract('dots.jpeg', 360)
#    for color in colors:
#        print(f"{color.rgb[0], color.rgb[1], color.rgb[2]}")
#        pallette.append((color.rgb[0], color.rgb[1], color.rgb[2]))
    print(f"{len(pallette)}")
    korni = t.Turtle()
    t.colormode(255)
    korni_screen  = t.Screen()
    korni.speed("fastest")
    count = 0
    korni.hideturtle()
    korni.penup()
    x = -250
    y = -250
    korni.setposition(x, y)
    for row in range (10):
        for col in range(10):
            korni.dot(20, random.choice(pallette)) 
            korni.fd(50)
        y += 50
        korni.setposition(x, y)
    korni_screen.exitonclick() 