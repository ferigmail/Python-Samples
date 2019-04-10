Q=[-3,4,7,8,9,11,12,14,15,25]
p=0     # it does not matter what u put for p or even define it here
        # u just need to define a global variable inside the def and then
        # print that out of def otherwise u can not print local out side of def
try:
    b=int(input('enter a number'))
    def b_search(a,b):
        l=0
        u=len(a)  # if u say u=len(a)-1 then it can not find the last index of list=25
        i=0
        while l<=u and i<len(a):
            mid=(l+u)//2
            if a[mid]==b:
                globals()['p']=mid+1
                return True
            else:
                if a[mid]<b:
                    l=mid
                else:
                    u=mid
            i+=1
        return False
except:
    print('it is not an int number')
if b_search(Q,b):
    print(b,'is found at',p,'of list')
else:
    print(b, 'is not found in the list')