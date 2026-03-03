num=int(input("enter the num: "))
def tables(num):
    for i in range(11):
        print(f"{num}x{i}={num*i}")
def repeat(num):
    for i in range(num):
        print(f"this number made me repeat {num} times")
print("1.Tables \n 2.Repeat")
option=int(input("enter the option"))
if option==1:
    tables(num)
elif option==2:
    repeat(num)
else:
    print("tm manege hogu")
    
    