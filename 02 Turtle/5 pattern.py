from turtle import *

pencolor("black")
pensize(2)
fillcolor('blue')
speed('fastest')

for i in range(28,0,-1):
    begin_fill()
    circle(i*6)
    left(30)
    end_fill()

mainloop()