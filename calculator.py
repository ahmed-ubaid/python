import math
def add(a,b):
    return a+b;

def sub(a,b):
    return a-b;

def mul(a,b):
    return a*b;

def div(a,b):
    while(b==0):
        b=int(input("Enter valid value for the divisor: ").strip())
    return a/b;

def powe(a,b):
    return math.pow(a,b);

def sqrt(a):
    while(a<0):
        a=int(input("Invalid value of parameter please enter a valid value"))
    return math.sqrt(a) 

print(div(-12,0))