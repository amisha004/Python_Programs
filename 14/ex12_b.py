import turtle
t=turtle.Turtle()
t.width(2)
t.color("#FFFFFF")
new=turtle.getscreen()
t.speed(-1)
new.bgcolor("black")
def squre(length, angle):
    t.forward(length)
    t.right(angle)
    t.forward(length)
    t.right(angle)
    t.forward(length)
    t.right(angle)
    t.forward(length)
    t.right(angle)
    squre(80, 90)
    for i in range(36):
        t.right(10)
        squre(80, 90)