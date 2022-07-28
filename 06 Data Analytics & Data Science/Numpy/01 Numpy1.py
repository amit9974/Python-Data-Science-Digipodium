import numpy as np

a = [1,2,3,4,5]
a = np.array(a)

print(a)
print(type(a))
print(a.shape) # check row and column

# 2d array
b = [[1,2,3],[4,3,5]]
b = np.array(b)
print(b)
print(b.shape)

c = [[[1,2,3],[3,2,1],[1,2,3]],[[1,2,3],[4,5,6],[1,2,5]]]
c = np.array(c)
print(c)
print(c.shape)

z = np.zeros((4,3))
print(z)

z = np.zeros((4,3),dtype=int)
print(z)

o = np.ones((4, 5), dtype=int)
print(o)

t = np.arange(-10,10)
print(t)
print(t.shape)

t1 = np.arange(-20,20,.25)
print(t1)

t2 = np.linspace(-10,10,50)
print(t2.shape)
print(t2)

t3 = np.logspace(-10,10,30)
print(t3.shape)
print(t3)

t4 = np.unique(1,2,3,21)
print(t4)

x = np.arange(-np.pi, np.pi, .02)
print(x.shape)

x2 = x.reshape((5, 63))
print(x2)

random1 = np.random.random((4,5))
print(random1)

random2 = np.random.randint(0,100,(5,5))
print(random2)

a = np.random.randint(1,10,(3,3))
b = np.random.randint(1,10,(3,3))

print(a + b)
print(a * b)
print(a-b)
print(a/b)

np.cross(a,b)
np.dot(a,b)
np.cumprod(a)
a.mean()
a.mean(axis=0)
a.mean(axis=1)
np.median(a)
print(np.median(a, axis=0)) #median along the column
print(np.median(a, axis=1)) # median along the rows

np.cos(a)
np.sin(a)