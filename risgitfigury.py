""" несколько закрашенных фигур"""
import turtle

square = turtle.Turtle()
square.hideturtle()
square.color('blue')
square.speed(10)
square.begin_fill()
for i in range(4):
    square.forward(100)
    square.right(90)
square.end_fill()
square.penup()
turtle.exitonclick()
turtle.mainloop()