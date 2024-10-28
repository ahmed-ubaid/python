list1=['⬛','⬛','⬛']
list2=['⬛','⬛','⬛']
list3=['⬛','⬛','⬛']
listmain=[list1,list2,list3]
print(listmain[0])
print(listmain[1])
print(listmain[2])

print("Where do you want to hide your tresure: ")
Row=int(input('Enter row: '))
Col=int(input('Enter column: '))

listmain[Row-1][Col-1]='x'

print(listmain[0])
print(listmain[1])
print(listmain[2])




