# import Python_Turtle
import turtle

#Создание окна
#Creating a window 
turtlePen = turtle.Turtle()
window = turtle.Screen()

#Цвет окна
#Window color
window.bgcolor("black")
 
#Метод отрисовки
#Rendering method 
def polygon(n, size=80):
    if n > 2:
        angle = 360 / n
 
        for n in range(0, n):
            turtlePen.pensize(1)
            turtlePen.color(colors[n % 5])
            turtlePen.left(angle)
            turtlePen.forward(size)

#Скорость отрисовки
#Rendering speed
turtlePen.speed(999)
 
#Массив цветов
#Array of colors
colors = ['white','cyan','blue', 'green', 'red']
 
size = 40

#Отрисовка объектов и выбор цвета
#Drawing objects and color selection
for i in range (0, 60):
	turtlePen.color(colors[i % 5])
	polygon(4, size)
	turtlePen.left(5)
	size = size + 1

#Обновление окна
#Updating the window
windows.mainloop()
