import random

listStr=input("enter the name of everyone present: ")
list1=listStr.split(",")

listLen=len(list1)

random_int=random.randint(0,listLen-1)
pay=list1[random_int]
print(f"{pay} will pay the bill")