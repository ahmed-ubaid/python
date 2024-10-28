
def isLeapYear(y):
    if((y%4==0) and (y%100!=0 or y%400==0)):
        return True
    else:
        return False

days=[31,28,31,30,31,30,31,31,30,31,30,31]

def howManyDays(y,m):
    if(isLeapYear(y) and m==2):
        return 29
    else:
        return days[m-1]

print(howManyDays(2004,2))
print(howManyDays(2004,1))
print(howManyDays(2002,2))



