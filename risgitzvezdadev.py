""" девятиконечная звезда"""
import turtle
nineang = turtle.Turtle()
for i in range(9):
    nineang.forward(120)
    nineang.left(140)
    nineang.forward(100)
    nineang.right(100)
turtle.exitonclick()
turtle.mainloop()