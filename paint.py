import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Simple Paint Game")
screen.bgcolor("white")

# Create the turtle for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.width(5)

# Function to change the color of the pen
def change_color_red():
    pen.color("red")

def change_color_blue():
    pen.color("blue")

def change_color_green():
    pen.color("green")

def change_color_black():
    pen.color("black")

# Function to draw
def draw(x, y):
    pen.goto(x, y)

# Function to lift the pen
def pen_up():
    pen.penup()

# Function to put the pen down
def pen_down():
    pen.pendown()

# Bind the functions to the screen
screen.listen()
screen.onscreenclick(draw)
screen.onkey(change_color_red, "r")
screen.onkey(change_color_blue, "b")
screen.onkey(change_color_green, "g")
screen.onkey(change_color_black, "k")
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "d")

# Keep the window open
turtle.done()
