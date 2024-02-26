""" круг и точка """
import turtle

turtle.title("Turtle Drawing") #
circle = turtle.Turtle() #
circle.shape("turtle") # черепашка
circle.pensize(10) #  толщина круга
circle.pencolor("red") #  цвет всего рисунка

circle.dot(20) # 
circle.penup() # подьем черепашки перед премещением
circle.goto(0, -100) # координаты центра круга
circle.pendown() # опускание черепашки после перемещения
circle.circle(100) # координата размещения точки 
turtle.exitonclick() #
