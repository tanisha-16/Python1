n=int(input("enter a number"))
temp=n
r=0
while(n>0):
    sum=n%10
    r=r+sum*sum*sum
    n=n//10
if(temp==r):
    print("the no. is armstrong")
else:
    print("the no. is not armstrong")