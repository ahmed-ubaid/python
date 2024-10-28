import math

num=int(input("Enter a number: "))

def ifPrime(n):
    sqrNum= math.ceil(math.sqrt(num))
    for i in range(2,sqrNum,1):
        if(n%i==0):
            return True
        else:
            return False

fi=ifPrime(num)

if fi:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")

