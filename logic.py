x=int(input("enter the number of heads"))
y=int(input("enterno of legs"))
if(y%2!=0):
    print("invalid")
else:
    r=(y-(2*x))//2
    c=(x-r)
    print(r,c)