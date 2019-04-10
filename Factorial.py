def fact(n):
    if n<0:
        return('not taking negative number')
    elif n==0:
        return 1
    return n* fact(n-1)
print(fact(9))
