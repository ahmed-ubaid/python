print("LOVE CALCULATOR")
yourName=input("Enter your full name: ").lower()
otherName=input("Enter the other person's full name: ").lower()
mainStr=yourName+otherName

str1='true'
perstr1=0
i=0
while(i<len(str1)):
    perstr1+=mainStr.count(str1[i])
    i+=1


str2='love'
perstr2=0
j=0
while(j<len(str2)):
    perstr2+=mainStr.count(str2[j])
    j+=1

lovePer=int(str(perstr1)+str(perstr2))

if(lovePer<10 or lovePer>90):
    print(f"Your love score is {lovePer}. you go together like coke and mentos")
elif(lovePer>40 and lovePer<50):
    print(f"Your love score is {lovePer}. You guys are ok together")
else:
    print("Your love score is {lovePer}.")




