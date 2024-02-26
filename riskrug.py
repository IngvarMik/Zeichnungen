""" рисунок круга с пояснениями"""
import turtle

turtle.title("Turtle Circles")# я так понимаю обьявили класс
circ = turtle.Turtle() # создали экземпляр класса Turtle под именем circ. Все изменения сохраняются для класса circ;
circ.pencolor("green") # цвет карандаша
circ.fillcolor("orange") # цвет заполнения круга
circ.shape("circle") # 
circ.pensize(5) # толщина карандаша - линии
circ.speed(10) # скорость выполнения рисунка
circ.fd(150) # вперед на 150 пикселей
circ.begin_fill() # начало заполнения
circ.circle(90) # круг радиус 90
circ.end_fill() # окончание заполнения

n = 10 # цикл который рисует круги спиральные
t = turtle.Turtle() # новая переменная класса turtle
while n <= 50: # пока п меньше равно 50 
    t.circle(n) # рисует круг
    n += 10 # с шагом 10 - итого 5 кругов

turtle.exitonclick()