x=int(input("enter the number"))
for i in range(2,x):
    if x%i==0:
        print('It is not prime')
        break
else:
    print("It is prime")

   


