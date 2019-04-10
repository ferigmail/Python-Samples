try:
    a = [-2, 0, 4, 8, 10, 11, 12, 15]
    def search(a,b):
            l = 0
            u = len(a)
            for i in range(len(a)):
                mid=(l+u)//2
                if a[mid]==b:
                    return True
                else:
                    if a[mid]<b:
                        l=mid
                    else:
                        u=mid

    if search(a,p):
        print('it is found')
    else:
        print('it is not found in the list')
except:
    print('invalid number')







