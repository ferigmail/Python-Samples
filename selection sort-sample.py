def sort(a):
    for i in range(len(a)-1):
        for j in range(i,len(a)):
            min=i
            if a[j]<a[min]:
                t=a[j]
                a[j]=a[min]
                a[min]=t

a=[1,5,3,2,8,7,10,-2]
sort(a)
print(a)
