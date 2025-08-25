import turtle
ventana= turtle.Screen()
n= turtle.Turtle()
n.shape("turtle")
n.shape("turtle")
n.color("green")
n.width(10)
n.speed(0)


import turtle
import random

pantalla = turtle.Screen()
pantalla.bgcolor("black")
pantalla.title("Tortuga impredecible")

tortuga = turtle.Turtle()
tortuga.speed(0)
tortuga.pensize(40)

def color_aleatorio():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

pantalla.colormode(255)

while True:
    color = color_aleatorio()
    tortuga.color(color)
    distancia = random.randint(20, 100)
    angulo = random.randint(0, 360)
    tortuga.forward(distancia)
    tortuga.left(angulo)

tortuga.hideturtle()
pantalla.mainloop()