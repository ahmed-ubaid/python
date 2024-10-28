import random

arr1=[1,2,3,4,5,6,7,8,9,0]
arr2=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
arr3=["!","@","#","$","%","^","&","*","(",")"]

totin=int(input("Enter the nmber of character you want in your password: "))
alpin=int(input("Enter the nmber of alphabets you want in your password: "))
numin=int(input("Enter the nmber of numbers you want in your password: "))
sigin=int(input("Enter the nmber of symbols you want in your password: "))

password_list=[]
password=''
for n in range(0,alpin):
    let=random.randint(0,len(arr2)-1)
    password_list+=arr2[let]
print(password_list)
for i in range(0,numin):
    let=random.randint(0,len(arr1)-1)
    password_list.append(arr1[let])

for i in range(0,sigin):
    let=random.randint(0,len(arr3)-1)
    password_list+=arr3[let]


for n in range(0,totin):
    let=random.randint(0,len(password_list)-1)
    temp=password_list[let]
    password_list[let]=password_list[n]
    password_list[n]=temp
    

for n in range(0,len(password_list)):
    password+=str(password_list[n])


print(password)

    


