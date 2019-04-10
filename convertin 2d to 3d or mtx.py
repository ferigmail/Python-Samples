from numpy import *
a=array([1,2,3,4,3,2,7,8,9,10,-10,11],int)
print(a)
b=a.reshape(3,4)
print(b)
print(b[0,3])
print(b.max())
for i in b:
    print(pow(i,2))
c=b.reshape(2,2,3)
print(c)
print(3*c)
print(sin(c))
print(c.max())
print(c.max())
print(c.min())
print(c)
print(c[1,0])
print(c[1,0,1])
for i in c:
    print(pow(i,2))
m=matrix('1 2 3 5; 2 3 5 6; 6 7 8 9')
r=matrix('2 3 4 7;-1 -3 0 1;-9 2 4 5')
print(m)
print(m+r)
print(m*3)
print(sin(m))
print(m.max())
print(r)
print(r[2,0])





