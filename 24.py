marks=input("Enter the marks of the student ").split()
maxN=0
for mark in marks:
    if(maxN<int(mark)):
        maxN=int(mark)

print(maxN)

# for n in range(10,5):
#     print(n)

# print('hi')