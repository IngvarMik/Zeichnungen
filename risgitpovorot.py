""" поворотные квадратики"""
import turtle

square = turtle.Turtle() # прямоугольная площадт - фигура
square.shape("turtle") # черепашка
square.color('red', 'green') # ред - цвет линий , грин - цвет заполнения квадратов
square.begin_fill() # начало заполнения
for j in range(18): # цикл - 18 полных фигур 
    square.left(20) #  поворот всей площадки двадцать раз налево
    for i in range(4): #
        square.forward(100) # вперед 100 пикселей
        square.left(90) # поворот налево на 90 градусов

square.end_fill() # конец заполнения
turtle.exitonclick() #