# startp=int(input("Enter a starting point: "))
# endp=int(input("Enter the end point: "))+1
# sumE=0
# for n in range(startp,endp):
#     if(n%2==0):
#         sumE+=n
#     else:
#         pass

# print(sumE)

for n in range(1,100):
    if(n%3==0):
        if(n%5==0):
            print("fizzbuzz")
        else:
            print("fizz")
    elif(n%5==0):
        print("buzz")
    else:
        print(n)

