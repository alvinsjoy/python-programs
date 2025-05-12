import numpy as np
from numpy.linalg import inv, det
import matplotlib.pyplot as plt
import math

arr = np.array([[(1,2,3,4), (4,5,6, 7)], 
                [(7,8,9,10), (10,11,12,13)], 
                [(13,14,15,16), (13,14,15,16)], 
                [(16,17,18,19), (16,17,18,19)]])
print(arr.shape)
print(arr.ndim)
print(arr.size, arr.shape[0] * arr.shape[1] * arr.shape[2])

a = np.arange(10)
a[0:3] = 5
print(a)
a[:] = 200
print(a)

b = np.arange(10)
b = b + 1
print(b)

c = np.array([[1, 2], [3, 4]])
d = c.transpose()
print(d)

brr = np.array([[1, 2], [3, 4]])
crr = inv(brr)
print(crr)
print(np.dot(brr, crr))
print(crr.dot(brr))

drr = np.trace(c)
print(drr)

A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
B = np.array([[5, 6, 2], [8, 32, 2], [2, 5, 2]])
print(det(A))
C = np.dot(A, B)
print(C)

lol = np.random.randint(2, 10, size= 9)
print(lol)

lol = np.random.randint(2, 20, size= (4, 5))
print(lol)

l = np.random.choice([1, 3, 5, 2, 5, 8, 11, 3, 4, 5], size = (5, 3))
m = np.random.choice([1, 3, 5, 2, 5, 8, 11, 3, 4, 5])
print(m)
print(l)
l = np.array([1, 3, 5, 2, 5, 8, 11, 3, 4, 5])
np.random.shuffle(l)
print(l)

print(np.random.rand())
print(np.random.rand(2, 3))

print(np.random.permutation(l))
# same as below
print(np.random.choice(l, size = np.shape(l), replace = False))

x = np.arange(0, math.pi * 2, 0.05)
plt.plot(x, np.sin(x), 'r-', label='sine')
plt.plot(x, np.cos(x), 'b--', label='cosine')
plt.plot(x, -np.sin(x), 'g:', label='negative sine')
plt.plot(x, -np.cos(x), 'y--', label='negative cosine')
plt.title("Sine, Cosine, -ve Sine and -ve Cosine")
plt.xlabel("Angle in radians")
plt.ylabel("Value")
plt.legend(loc = "upper right")
plt.show()

x = np.array([2, 5, 4, 2, 8, 4, 9, 11, 10, 12, 8, 4, 9, 9, 12])
y = np.arange(0, 15)
plt.bar(x, y, color = "red")
plt.show()

plt.hist(x)
plt.show()

plt.scatter(x, y)
plt.show()

plt.stem(x, y)
plt.show()

plt.pie(x, labels = y)
plt.show()