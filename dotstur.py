import turtle

dots=turtle.Turtle()

dotdist=30
hght=8
widt=5

dots.penup()
for x in range(hght):
    for y in range(widt):
        dots.dot()
        dots.forward(dotdist)
    dots.backward(dotdist*widt)
    dots.right(90)
    dots.forward(dotdist)
    dots.left(90)

