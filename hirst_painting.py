import random
import turtle as t
from turtle import Screen
from random import choice
import colorgram

tim = t.Turtle()
tim.penup()
tim.hideturtle()
screen = Screen()
screen.colormode(255)
tim.speed('fastest')

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

# rgb_colour = []
# colors = colorgram.extract('imp.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colour.append(new_color)
#
# print(rgb_colour)

colour_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216),
               (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
               (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28),
               (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199),
               (179, 17, 8), (233, 66, 34)]

number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()