#PIZZA ORDER
print("Welcome to the pizza shop please state your order.")
pizzaSize=input("Please tell us what size pizza do you want S:7$ M:10$ L:13$ XL:16$ ")
peproni=input("Would you like to add pepperoni? yes or no ")
cheese=input("Would you like to add cheese? yes or no ")
total=0


if(pizzaSize=='s'):
    total=7
    if(peproni=='yes'):
        total+=1

elif(pizzaSize=='m'):
    total=10
    if(peproni=='yes'):
        total+=1

elif(pizzaSize=='l'):
    total=13
    if(peproni=='yes'):
        total+=2
        
else:
    total=16
    if(peproni=='yes'):
        total+=3

if(cheese=='yes'):
    total+=2

print(f"Your total would be {total} ")


