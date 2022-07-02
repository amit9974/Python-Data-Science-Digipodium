from turtle import *
import random
colors = ['blue','pink']
speed('fastest')
for i in range(50):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    penup()
    goto(x,y)
    pendown()
    pensize(random.randint(1,2))
    pencolor(colors[random.randint(0,1)])
    radius = random.randint(5,30)
    fillcolor('red')
    begin_fill()
    for i in range(6):
        circle(radius)
        left(60)
    end_fill()
mainloop()