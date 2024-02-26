""" рисуем квадрат и звезду"""
import turtle
turtle.shape("turtle")
square = turtle.Turtle() # 
for i in range(4): # цикл для рисунка квадрата
    square.forward(100)# вперед на 100 пикселей
    square.right(90)# направо на 90 градусов

starf = turtle.Turtle()#
for i in range(5):# цикл для рисунка звезды
    starf.forward(100)# вперед на 100 пикселй
    starf.right(144)# поворот направо на 144 градуса

turtle.exitonclick()
turtle.mainloop()