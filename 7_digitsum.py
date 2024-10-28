'''
num=input("Enter a 2 digit number: ")
print(num)
d1=str(num[0])
d2=str(num[1])
print(int(d1)+int(d2))
'''
print("\n following will be done by using while\n")

num2=input("Enter a number: ")
print(num2)
intnum2=123
sumOfDigits=0
digit=0
while(intnum2!=0):
    digit=int(intnum2%10)
    sumOfDigits=sumOfDigits+digit
    intnum2=intnum2/10

print(sumOfDigits)