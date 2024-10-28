height=int(input("Please enteryour height "))
price=0
if(height>120):
    age=int(input("Please enter your age "))
    photo=input("Would you like to take a picture during your ride? yes or no ")
    if(age<12):
        price=2
    elif(age<18):
        price=5
    elif(age>45 and age<55):
        price=0
    else:
        price=7

    if(photo=='yes'):
        if(age>45 and age<55):
            price=0
            print("Yor ride will be free of cost")
        else:
            price+=3
            print(f"Your total would be {price}$ ")
    else:
        print(f"Your total would be {price}$ ")

else:
    print("Sorry,you can not ride the rollercoster.")

