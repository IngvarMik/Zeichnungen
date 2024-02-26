""" рисунок круга с заданным количеством точек на нем"""
""" t."""
from turtle import *
t = Turtle()
t.screen.setup(800, 800)
def circ(d, r, rBig):
    for i in range(d):
        t.circle(rBig, 360 / d )
        t.dot(15, "red") # команда точки , причем еще и с указанием цвета - ред и радиуса самой точки
t.up()
t.goto(250, 0)
t.setheading(90)
t.down()
circ(45, 10, 200)
t.screen.exitonclick()
t.screen.mainloop()