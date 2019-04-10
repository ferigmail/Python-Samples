def sort(self):
    for i in range(0,len(a)):
        min = i
        for j in range(i,len(a)):
            if a[min] > a[j]:
                min=j
        t = a[i]
        a[i] = a[min]
        a[min] = t

a=[1,5,0,9,-8,4]
sort(a)
print(a)