""" рисование выпуклых многосторонних многоугольников"""
import turtle

polygon = turtle.Turtle() #
num_sides = 5 # количество граней
side_length = 100 # длина грани
angle = 360.0 / num_sides #  угол поворота

for i in range(num_sides): # цикл
    polygon.forward(side_length) # в цикле вперед на side_length пикселей 
    polygon.right(angle) # поворот на angle градусов

turtle.exitonclick()
