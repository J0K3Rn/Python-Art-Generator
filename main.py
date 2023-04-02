from turtle import Turtle, Screen
import colorgram
import random

# Adjustable image variables
global_row_length = 10
num_of_colors = 50
image_file = 'img.jpeg'


# Declarations
painter = Turtle()
painter.shape('classic')
painter.penup()
painter.speed("fastest")
painter.hideturtle()
screen = Screen()
screen.colormode(255)
color_list = []


def set_start_pos():
    painter.setposition(global_row_length * -23, global_row_length * -23)


def pick_colors():
    colors = colorgram.extract(image_file, num_of_colors)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        color_list.append(new_color)


def reset_row(row_length):
    painter.left(90)
    painter.forward(50)
    painter.left(90)
    painter.forward(50 * row_length)
    painter.left(180)


def random_color():
    return random.choice(color_list)


def draw_row(length):
    for _ in range(length):
        painter.dot(20, random_color())
        painter.forward(50)


def main():
    set_start_pos()
    pick_colors()
    for i in range(global_row_length):
        draw_row(global_row_length)
        reset_row(global_row_length)
    screen.exitonclick()


if __name__ == "__main__":
    main()

