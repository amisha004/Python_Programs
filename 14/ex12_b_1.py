import turtle
# Set up the turtle window and colors
turtle.setup(width=600, height=600)
turtle.bgcolor('black')
turtle.pensize(3)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# Draw a square
for i in range(4):
    turtle.pencolor(colors[i])
    turtle.forward(100)
    turtle.left(90)
# Draw a circle by incrementally increasing the sides of the square
for i in range(4, 100):
    turtle.pencolor(colors[i % len(colors)])
    turtle.circle(i)    
# Hide the turtle and exit when the user clicks the window
turtle.hideturtle()
turtle.exitonclick()
