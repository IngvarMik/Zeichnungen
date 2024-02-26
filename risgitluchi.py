""" расходящиеся лучи"""
import turtle

spiral = turtle.Turtle()
for i in range(30): # цикл 
    spiral.fd(i * 10) # вперед на i*10 пикселей
    spiral.rt(45) # поворот на 45 градусов
    spiral.goto(0,0) # возврат в нулевую точку 
turtle.exitonclick() #