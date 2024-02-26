"""поворот  - t.left"""
from turtle import *
t = Turtle()
t.screen.setup(800, 800)
def rectangle(w, h):# рисунок прямоугольника команда restangle
    for i in range(2): # цикл 
        t.left(90) # поворот влево на 90 градусов
        t.fd(h)
        t.left(90)# поворот влево на 90 градусов
        t.fd(w)        
rectangle(320, 200)
t.screen.exitonclick()
t.screen.mainloop()