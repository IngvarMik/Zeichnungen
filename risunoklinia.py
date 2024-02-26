from turtle import * # стандартная формула запуска turtle
t = Turtle ()           # черепашка
t.screen.setup(800,800) # рисунок квадрата экрана
t.fd(200)  # рисунок линии
t.left(90) # поворот налево 
t.fd(300) # опять линия
t.left(120)
t.fd(250)
t.screen.exitonclick() # 
t.screen.mainloop() # остановка программы