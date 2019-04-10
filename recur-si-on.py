import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2500)
i=0
def f():
    global i
    i+=1
    print('far',i)
    f()
f()

