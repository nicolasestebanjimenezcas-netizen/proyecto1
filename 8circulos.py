import turtle
ventana= turtle.Screen()
t= turtle.Turtle()
t.color("green")
t.speed(0)


for i in range(8):
    t.circle(100)
    t.left(45)

t.write("flor", font=("Arial", 30, "normal"))
turtle.done()