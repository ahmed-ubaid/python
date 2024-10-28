#CHEXK IF NUM ODD OR EVEN
num=int(input("Enter a number :"))

if(num%2==0):
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

'''
the inefficient way
while(num>=2):
    num=num-2

if(num==1):
    print(f"{num} is an odd number")
else:
    print(f"{num} is an  even number")
'''
