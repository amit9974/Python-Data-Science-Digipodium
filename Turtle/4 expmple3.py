import mailcap
from turtle import *

s = getscreen()
t = Turtle()
t.speed("fastest")

for i in range(8):
    t.pensize(2)
    t.fd(100)
    t.circle(50,180)
    t.lt(360/4)
    t.dot(15)
mainloop()