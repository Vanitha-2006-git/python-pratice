num=int(input("enter the number"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not prime number")
        else:
            print(num,"is prime num")
else:
    print(num,"is not prime num")