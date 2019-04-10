a=[]
for i in range(3):
    x=str(input('enter next string'))
    a.append(x)
print(a)

def count():
    c = 0
    s = 0

    for i in a:
        if len(i)>2:
            c+=1
        else:
            s+=1
    print('the number of string with more than 2 letteres is:{}'.format(c))
count()
