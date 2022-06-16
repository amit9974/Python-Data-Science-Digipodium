from turtle import *

colors=['red','blue','yellow','green']
t = Turtle()
bgcolor('black')
t.speed('fastest')

for i in range(160):
    t.color(colors[i%4])
    t.width(i//100 + 2)
    t.rt(45)
    t.lt(-85)
    t.fd(i*2)
    # t.bk(i)
mainloop()