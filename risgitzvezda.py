"""звезда восьмилучевая """
import turtle
star = turtle.Turtle()
star.hideturtle() # 
for i in range(8): #
    star.forward(200) #
    star.right(135) #
turtle.exitonclick()
turtle.mainloop()