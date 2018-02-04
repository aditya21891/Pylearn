# this is a program to wish Happy Birthday using Turtle

import turtle

arun=turtle.Turtle()
arun.width(8)
arun.color("red")
new=turtle.getscreen()
arun.speed(4)

new.bgcolor("lightblue")

# Hidden Work(penup)
arun.left(180)
arun.penup()
arun.forward(300)
arun.right(90)
arun.forward(100)
arun.pendown()

# Printing H


#start to draw
arun.forward(50)
arun.right(90)
arun.forward(50)
arun.left(90)
arun.forward(50)
arun.left(90)

arun.penup()
arun.forward(50)
arun.left(90)
arun.pendown()
arun.forward(50)
arun.left(90)
arun.forward(50)
arun.right(90)
arun.forward(50)


# printing A

arun.penup()
arun.left(90)
arun.forward(15)
arun.pendown()
arun.left(70)
arun.forward(110)
arun.right(70)
arun.right(70)
arun.forward(110)
arun.left(180)
arun.forward(55)
arun.left(70)
arun.forward(38)
arun.left(70)
arun.penup()
arun.forward(55)
arun.left(110)

arun.forward(100)

# printing P

arun.left(90)
arun.pendown()
arun.forward(100)
arun.right(90)
arun.forward(50)
arun.right(20)
arun.forward(20)
arun.right(70)
arun.forward(40)
arun.right(70)
arun.forward(20)
arun.right(20)
arun.forward(50)
arun.left(90)
arun.forward(50)
arun.left(90)
arun.penup()
arun.forward(100)


# printing P

arun.left(90)
arun.pendown()
arun.forward(100)
arun.right(90)
arun.forward(50)
arun.right(20)
arun.forward(20)
arun.right(70)
arun.forward(40)
arun.right(70)
arun.forward(20)
arun.right(20)
arun.forward(50)
arun.left(90)
arun.forward(50)
arun.left(90)
arun.penup()
arun.forward(100)

# printing Y

arun.forward(20)
arun.pendown()
arun.left(90)
arun.forward(50)
arun.left(30)
arun.forward(60)
arun.backward(60)
arun.right(60)
arun.forward(60)
arun.backward(60)
arun.left(30)

# go to Home

arun.penup()
arun.home()

arun.color("orange")
new.bgcolor("lightgreen")
# setting second row

arun.backward(300)
arun.right(90)
arun.forward(60)
arun.left(180)


# printing P


arun.pendown()
arun.forward(100)
arun.right(90)
arun.forward(50)
arun.right(20)
arun.forward(20)
arun.right(70)
arun.forward(40)
arun.right(70)
arun.forward(20)
arun.right(20)
arun.forward(50)
arun.backward(50)
arun.left(180)
arun.right(20)
arun.forward(20)
arun.right(70)
arun.forward(40)
arun.right(70)
arun.forward(20)
arun.right(20)
arun.forward(50)
arun.right(90)
arun.forward(10)


# go to Home

arun.penup()
arun.home()

# setting up

arun.backward(200)
arun.right(90)
arun.forward(10)
arun.left(90)
arun.pendown()
arun.forward(20)
arun.penup()
arun.home()

# D

arun.backward(150)
arun.right(90)
arun.forward(60)
arun.pendown()
arun.backward(100)
arun.right(90)
arun.forward(10)
arun.backward(70)
arun.left(180)
arun.right(20)
arun.forward(20)
arun.right(70)
arun.forward(88)
arun.right(70)
arun.forward(20)
arun.right(20)
arun.forward(70)

arun.penup()
arun.home()

# set up for A

arun.backward(50)
arun.right(90)
arun.forward(65)
arun.left(90)



# printing A


arun.pendown()
arun.left(70)
arun.forward(110)
arun.right(70)
arun.right(70)
arun.forward(110)
arun.left(180)
arun.forward(55)
arun.left(70)
arun.forward(38)
arun.left(70)
arun.penup()
arun.forward(55)
arun.left(110)

arun.forward(100)

# printing Y


# printing Y


arun.pendown()
arun.left(90)
arun.forward(50)
arun.left(30)
arun.forward(60)
arun.backward(60)
arun.right(60)
arun.forward(60)
arun.backward(60)
arun.left(30)

# go to Home 

arun.penup()
arun.home()


# settig pogition

arun.right(90)
arun.forward(215)
arun.right(90)
arun.forward(200)
arun.right(90)

#color

arun.color("green")
new.bgcolor("lightblue")

# printing A

arun.pendown()
arun.left(70)
arun.forward(110)
arun.right(70)
arun.right(70)
arun.forward(110)
arun.left(180)
arun.forward(55)
arun.left(70)
arun.forward(38)
arun.left(70)
arun.penup()
arun.forward(55)
arun.left(110)

arun.forward(100)

# design


#design pattern
arun.home()
arun.forward(200)
arun.pendown()
arun.color("hotpink")
arun.width(3)
arun.speed(0)

def squre(length, angle):
    
    arun.forward(length)
    arun.right(angle)
    arun.forward(length)
    arun.right(angle)
   
    arun.forward(length)
    arun.right(angle)
    arun.forward(length)
    arun.right(angle)

squre(80, 90)

for i in range(36):
      arun.right(10)
      squre(80, 90)




turtle.mainloop()
