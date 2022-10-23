def prime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True
x=int(input("Enter the range "))
y=int(input())
for i in range(x,y+1):
    if(prime(i)):
        print(i)
