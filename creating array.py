from array import*
x=array('i',[])
a=int(input("Enter the lenght of array"))
for i in range(a):
    y=int(input("Enter the next number"))
    x.append(y)
print(x)
b=int(input("the number you want to remove"))
k=0
for i in x:
    if i==b:
        print(k)
        x.remove(i)
        break
    k+=1
else:
    print('you enter a wrong number')
print(x)

