from array import *
a=array("i",[1,2,3,4])
b=array("i",[-1,-4,5,6])
print(a+b)
for i in a:
    y=pow(i,3)
    b.append(y)

print(b)
b.remove(-4)
print(b)
b.pop()
print(b)
print(max(b))
print(min(b))
print(sum(b))
b.insert(3,100)
print(b)