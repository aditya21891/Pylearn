# a function to draw a square
import turtle

draw=turtle.Turtle()

def square(length,angle):
    draw.forward(length)
    draw.right(angle)
    draw.forward(length)
    draw.right(angle)
    draw.forward(length)
    draw.right(angle)
    draw.forward(length)

square(100,90)
square(50,90)
