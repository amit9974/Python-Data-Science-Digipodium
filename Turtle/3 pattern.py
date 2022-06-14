from turtle import *
t = Turtle()
colors = ['green','orange','yellow','red','blue','purple']
t.speed('fastest')
bgcolor('black')

for i in range(260):
    t.color(colors[i%6])
    t.width(i//100 + 2)
    t.rt(75)
    t.fd(90)
    t.bk(75)
    t.lt(i)
mainloop()