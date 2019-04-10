from time import sleep
from threading import *
class A(Thread):
    def run(self):
        for i in range(5):
            print("Farzad")
            sleep(2)
class B(Thread):
    def run(self):
        for i in range(5):
            print("38")
            sleep(2)
a1=A()
b1=B()
a1.start()
sleep(1)
b1.start()
a1.join()
b1.join()
print("the operation is accomplished")