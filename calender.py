days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
month={
    "January":31,
    "February":28,
    "March":31,
    "April":30,
    "May":31,
    "June":30,
    "July":31,
    "August":31,
    "September":30,
    "October":31,
    "November":30,
    "December":31
}

calender={}
year={}
def isLeapYear(year):
    if((year%4==0) or (year%100!=0 and year%400==0)):
        return True
    else:
        return False
k=0
def yearIs():
    
    for n in month:
        mo={}
        for i in range(1,month[n]+1):
            mo.update({i:days[k]})  
            k=k+1
            if(k==7):
                k=0
        calender.update({n:mo})  

yearIs()

print(calender["January"][31])
