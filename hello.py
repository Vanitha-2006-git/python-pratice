print("HI")
x=5
y=6
x,y=y,x
print("x",x,"y",y)
num=90
if num%2:
    print("even number")
else:
    print("odd num")
    
num=int(input("Enter the number: "))
for i in range(1,11):
    print(num,"x", i,"=",num*i)
    
    n=int(input("enter the num"))
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
        print(fact)