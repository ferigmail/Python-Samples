a=[8,2,8,5,7,8,0,9]
class A:
    def search(self,a,n):
            self.n=n
            self.a=a
            i=0
            c=0
            while i<len(a):
                if a[i]==n:
                    c+=1
                else:
                    pass
                i+=1
            print("the repetition of the", n ,"is:",c)
b=A()
b.search(a,100)
x=[8,2,8,5,7,8,0,9]
class B:
    def search(self,b,n):
        self.b=b
        self.n=n
        c=0
        for i in b:
            if i==n:
                c+=1
            else:
                pass
        print(c,'times', n, 'has been repeated in this list')
c=B()
c.search(x,0)



