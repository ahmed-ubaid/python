days=["Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"]
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
year={}
def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def yearCalender():
    k=0
    for m in range (1,2099):
        calender={}
        if(isLeapYear(m)):
            month["February"]=29
        else:
            month["February"]=28
        
        for n in month:
            mo={}
            for i in range(1,month[n]+1):
                mo.update({i:{"day":days[k],"event":{}}})  
                k=k+1
                if(k==7):
                    k=0
            calender.update({n:mo})
        year[m]=calender
yearCalender()

def howManyXday(n,xday):
    count=0
    for m in year[n]:
        for d in year[n][m]:
            if(year[n][m][d]["day"]==xday):
                count=count+1

    return(count)



year[2001]["September"][14]["event"]="birthday"
print(year[2001]["September"][14]["event"])

'''
event{
    birthday:["ubaid","abeed"],
    today:{
        name:{time,venue},
    }
}
'''