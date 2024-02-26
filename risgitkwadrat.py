"""рисуем квадрат"""
import turtle
square = turtle.Turtle()
square.shape("turtle") #cизображение черепашки
for i in range(4): # цикл четыре раза
    square.forward(150) # вперед на 100 пикселей
    square.right(90) # поворот направо на 90градусов
turtle.exitonclick()
turtle.mainloop()