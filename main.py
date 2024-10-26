import turtle as t
import random
import colorgram

colours = colorgram.extract("image.jpg", 25)

rgb_colours = []
for colour in colours:
    # rgb_colours.append(colour.rgb[:]) OR
    rgb_colours.append(tuple(colour.rgb))

rgb_colours.pop(0)
# removes item at the specified index.
# As colours are sampled in order of occurrence frequency,
# the first colour is likely to be a background shade of white
print(rgb_colours)

turtle = t.Turtle()
t.colormode(255)
turtle.penup()
turtle.shape("circle")
y_cor = -250

for row in range(10):
    turtle.goto(-225, y_cor)
    y_cor += 50
    for n in range(10):
        turtle.dot(20, random.choice(rgb_colours))
        turtle.forward(50)

turtle.hideturtle()

screen = t.Screen()
screen.exitonclick()
