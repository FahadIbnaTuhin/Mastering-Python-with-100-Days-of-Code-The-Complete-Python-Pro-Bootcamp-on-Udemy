# import colorgram
#
# listing = []
# colors = colorgram.extract('pic.jpg', 30)
# for i in colors:
#     # r = i.rgb.r
#     # g = i.rgb.g
#     # b = i.rgb.b
#     # tupleee = (r, g, b)
#     tupleee = (i.rgb.r, i.rgb.g, i.rgb.b)
#     listing.append(tupleee)
#
# print(listing)

import random
from turtle import Turtle, Screen, colormode

color_list = [(135, 167, 190), (208, 157, 108), (197, 144, 166), (31, 110, 168), (231, 215, 89), (126, 75, 92),
              (28, 136, 67), (187, 178, 19), (55, 19, 28), (145, 18, 38), (39, 176, 115), (225, 171, 195),
              (117, 187, 145), (229, 78, 52), (169, 71, 47), (35, 16, 15), (234, 220, 5), (189, 88, 106), (9, 100, 54),
              (20, 20, 28), (33, 167, 192), (184, 185, 212), (154, 214, 177), (238, 170, 156), (150, 22, 15),
              (90, 123, 184)]


colormode(255)

timmy = Turtle()
number_of_dots = 100
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()
