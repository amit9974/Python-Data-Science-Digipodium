from turtle import *

colors = ['red','blue','green','orange','yellow','purple']
s = getscreen()
t = Turtle()
bgcolor('black')

for i in range(360):
    t.color(colors[i%6])
    t.width(i//100 + 2)
    t.lt(59)
    t.fd(i)
mainloop()
