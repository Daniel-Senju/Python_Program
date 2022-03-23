# Python_Turtle
import turtle
 
turtlePen = turtle.Turtle()
window = turtle.Screen()
 
window.bgcolor("black")
 
 
def polygon(n, size=80):
    if n > 2:
        angle = 360 / n
 
        for n in range(0, n):
            turtlePen.pensize(1)
            turtlePen.color(colors[n % 5])
            turtlePen.left(angle)
            turtlePen.forward(size)

def polygon1(m, size1=80):
    if m > 2:
        angle1 = 360 / m
 
        for m in range(0, m):
            turtlePen.pensize(3)
            turtlePen.color(color1)
            turtlePen.left(angle1)
            turtlePen.forward(size1) 
 
turtlePen.speed(999)
 
colors = ['white','cyan','blue', 'green', 'red']
color1 = ["black"]
 
size = 40
size1 = 120
 
for i in range (0, 60):
	turtlePen.color(colors[i % 5])
	polygon(4, size)
	turtlePen.left(5)
	size = size + 1

for i in range (0, 80):
	turtlePen.color(color1)
	polygon1(4, size1)
	turtlePen.right(1)
	size1 = size1 - 1

windows.mainloop()
