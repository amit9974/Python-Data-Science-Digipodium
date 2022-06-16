from turtle import *

s = Screen()
s.setup(500,500)
bgcolor('black')
pencolor('blue')

for i in range(5):
    lt(72)
    for i in range(5):
        fd(100)
        rt(144)
mainloop()