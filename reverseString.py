str=input("input a string ");
arr=[];
str2=""
print(len(str))
for n in range(len(str)-1,-1,-1):
    str2+=str[n]

print(str2)