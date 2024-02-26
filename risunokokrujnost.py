"""окружность полуокружность"""
from turtle import *
t = Turtle()
t.screen.setup(800, 800) # оазмер экрана
def sq_cr(side):
    for i in range(4):
        t.left(90)
        t.fd(side)
    t.bk(side / 2)
    t.circle(side / 2, 360) # команда окружности -- 360 - полная окружность , 180 - половина окружности
    t.left(180)
    t.circle(side / 4, 360) # side - это обозначение радиуса - side / 5 это радиус - пятая часть строны прямоугольника
sq_cr(150) # это side  - сторона квадрата
t.screen.exitonclick()
t.screen.mainloop()