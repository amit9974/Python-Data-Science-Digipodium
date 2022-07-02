from turtle import *

s = Screen()
s.setup(500,500)


fillcolor('blue')
pencolor('black')
for i in range(5):
    lt(72)
    penup()
    fd(90)
    pendown()
    begin_fill()
    circle(40)
    end_fill()
    penup()
    bk(90)
    pendown()
mainloop()