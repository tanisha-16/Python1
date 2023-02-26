n=int(input("enter any no."))
temp=n
r=0
while(n>0):
    sum=n%10
    r=r*10+sum
    n=n//10
if(temp==r):
    print("the no is pallindrome")
else:
    print("the no is not pallindrome")    