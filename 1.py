dictA={
    1:2,
    2:1
}

'''listA=[1,2,3,4]
print(listA[dictA[1]])

dictA[1]=0
print(listA[dictA[1]])

item=dictA.items()
print(item)'''

for value in dictA:
    print(value)

dictA.update({3:3,4:4})
print(dictA)

y=0
dictA.update({y:y})
print(dictA)
mydict={"apple":"apple",y:6}
dictA+=mydict
print(dictA)
