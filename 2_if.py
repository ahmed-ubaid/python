def capitalize(f_name,l_name):
     str=f_name[0].upper()
     
     for n in range(1,len(f_name)):
          str=str+f_name[n]

     str=str+" "+l_name[0].upper()

     for n in range(1,len(l_name)):
          str=str+l_name[n]

     return str

print(capitalize("ubaid","ahmed"))
     
def betterCapitalize(f_name,l_name):
     return f_name.title()+" "+l_name.title()

print(betterCapitalize("zAiD","ahmeD"))

