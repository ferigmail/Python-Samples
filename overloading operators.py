class Farzad:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __ge__(self,other):
        if self.m1>=other.m1 and self.m2>=other.m2:
            return("f1 is the winner")
        elif self.m1<other.m1 and self.m2<other.m2:
            return("f2 is the winner")
        else:
            return("can not compare")
    def __str__(self):
        return "{} {}".format(self.m1, self.m2)
f1=Farzad(25,46)
f2=Farzad(35,36)
print(f1>=f2)
print(f2)
print(f1)

