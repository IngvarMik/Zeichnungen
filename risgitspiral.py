""" спирали """
import turtle

spiral = turtle.Turtle() # переменная присваивается spiral
spiral.color ("red" ) # цвет линии

for i in range(60): # цикл  40 повторений
    spiral.forward(i * 10) # вперед на i * 10
    spiral.right(144) # поворот на 144 градуса

turtle.exitonclick()