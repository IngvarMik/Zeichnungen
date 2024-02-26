""" расклад фигур """
import turtle

turtle.hideturtle()
turtle.speed(10)
""" красный квадрат"""
turtle.color('red')
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.penup() # перемещение черепашки для начала нового рисунка
turtle.goto(200, 200)
turtle.pendown()
""" рисунок пятиконечная звезда зеленая  с заполнением"""
turtle.color('green')
turtle.begin_fill()
for i in range(5): # пятиконечная звезда зеленая
    turtle.forward(100)
    turtle.rt(144)
turtle.end_fill()

turtle.penup() # перемещение черепашки для начала нового рисунка
turtle.goto(-200, -150)
turtle.pendown()
""" звезда восьмиконечная синяя с заполнением"""
turtle.color('blue')
turtle.begin_fill()
for i in range(8): # восьмиконечная звезда синяя
    turtle.forward(100)
    turtle.right(135)
turtle.end_fill()

turtle.penup() # перемещение черепашки для начала нового рисунка
turtle.goto(200, -200)
turtle.pendown()
""" треугольник цвет циан """
turtle.color('cyan')
turtle.begin_fill()
for i in range(3): # треугольник 
    turtle.forward(100)
    turtle.lt(120)
turtle.end_fill()

turtle.penup() # перемещение черепашки для начала нового рисунка
turtle.goto(-200, 200)
turtle.pendown()
""" девятиконечная звезда цвет магента"""
turtle.color('magenta')
turtle.begin_fill()
for i in range(9): # девятиконечная звезда цикл
    turtle.forward(30)
    turtle.right(140)
    turtle.forward(30)
    turtle.left(100)
turtle.end_fill()

turtle.exitonclick()