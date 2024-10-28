#ELIF
height=int(input("What is your height? "))
price=0
if(height>120):
    age=int(input("What is your age? "))
    
    if(age<10):
        price=5
    elif(age<=14):
        price=7
    else:
        price=10
else:
    print("you can not ride")

print(f"your ticket will cost {price}")




