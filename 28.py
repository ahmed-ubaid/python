import math

h=int(input("Enter the height of the wall in m: "))
w=int(input("Enter the width of the wallin m: "))

coverage=4

def totalBuckets(height,width):
    return math.ceil(((height*width)/coverage))
#   return ((height*width)/coverage)


print(totalBuckets(height=h,width=w))


