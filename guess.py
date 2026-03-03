import random
secret_num=random.randint(1,50)
count=1
while True:
    guess=int(input("guess the number: "))
    print(secret_num)
    if guess==secret_num:
        print("you have guessed right!!")
    else:
        print("ohh no you miss it Try again!")
        count+=1
print(f"you have taken {count} trails")
        
        
        

