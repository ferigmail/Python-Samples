class A:
    Tel=200
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,x=None,y=None,z=None):
        s=0
        if x!=None and y!=None and z!=None:
            s=x+Y+z
        elif x!=None and y!=None:
            s=x+y
        else:
            s=x
        return s
    def __str__(self):
        return"{}  {}".format(self.m1,self.m2)


a=A(30,25)
print(a.sum(1))
print(a)