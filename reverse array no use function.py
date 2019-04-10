from array import *
a=array("i",[])
x=int(input("enter the lenght of your basket"))
for i in range(x):
    y=int(input('Enter the next Value'))
    a.append(y)
print(a)
c=array(a.typecode,a[::-1])
print(c)
