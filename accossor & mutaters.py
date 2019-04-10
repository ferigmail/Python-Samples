class NIDC:
    location='Ahwaz'
    Tel=403
    def __init__(self,name,position,salary,bonus):
        self.name=name
        self.position=position
        self.salary=salary
        self.bonus=bonus
    def  ave(self):
        return (self.salary+self.bonus)/2
    def get_salary(self):
        return self.salary
    def set_salary(self,value):
        self.salary=value
    @classmethod
    def get_place(cls):
         return cls.location

    @classmethod
    def set_place(cls,x):
        cls.location=x
    @staticmethod
    def all():
        print('hi')
e1=NIDC('farzad','Coordinator',10000,3000)
e2=NIDC('hossein','MWD',60000,1000)
e3=NIDC('peyman','DD',9000,2000)
print(e1.name,e1.salary,e1.location)
print(e1.get_salary(),e1.name)
e1.set_salary(14000)
print(e1.name,e1.salary,e1.location)
e1.set_place('arak')
print(e1.name,e1.salary,e1.location)
NIDC.set_place('amol')
print(e1.name,e1.salary,e1.location)
NIDC.all()
