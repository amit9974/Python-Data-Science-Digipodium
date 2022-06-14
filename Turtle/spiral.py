from turtle import *

a = getscreen()
t = Turtle()
bgcolor('black')
t.speed('fastest')
colors = ['red','green','blue','purple','pink','yellow']

for i in range(260):
    t.color(colors[i%6])
    t.width(i//100 + 2)
    t.lt(80)
    t.rt(-39)
    t.fd(5)
    t.bk(i*2)
mainloop()

