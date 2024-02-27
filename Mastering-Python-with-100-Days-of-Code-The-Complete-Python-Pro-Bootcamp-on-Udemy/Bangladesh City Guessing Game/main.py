import pandas
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("BD City Guessing Game")
image1 = "Photos/bd_edited.gif"
screen.addshape(image1)
image2 = "Photos/bd.gif"
screen.addshape(image2)
screen.setup(731, 900)
turtle.shape(image1)

# To get x and y coordinate
# def coordinate(x, y):
#     print(x, y)
# turtle.onscreenclick(coordinate)
# turtle.mainloop()

data = pandas.read_csv("bd_all_cities_name.csv")
cities_list = data.city.to_list()
print(cities_list)
user_corrected_cities = []

while len(user_corrected_cities) < 58:
    user_city = screen.textinput(f"{len(user_corrected_cities)}/58 Cities Guessed",
                                 "What's the next city name? ").title()
    # print(user_city)

    if user_city == "Exit":
        # For showing the correct picture
        screen.clear()
        turtle.shape(image2)

        # for giving the csv where you can get those city that you failed to guess
        # forgotten_city_list = []
        # for city in cities_list:
        #     if city not in user_corrected_cities:
        #         forgotten_city_list.append(city)
        # forgotten_city = pandas.DataFrame(forgotten_city_list)
        # forgotten_city.to_csv("forgottenCity.csv")
        break

    if user_city in cities_list and user_city not in user_corrected_cities:
        c = Turtle()
        c.penup()
        c.hideturtle()
        city = data[data.city == user_city]
        c.goto(city.x.item(), city.y.item())
        c.write(f"{user_city}", False, "center", ("Arial", 10, "normal"))
        user_corrected_cities.append(user_city)

screen.exitonclick()
