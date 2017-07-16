# a python program to draw a circle with square 
import turtle
draw=turtle.Turtle()

def square(length,angle):
    for i in range(4):
        draw.forward(50)
        draw.right(90)
    
for j in range(36):
    square(50,90)
    draw.right(10)
