import random

print("A coin has been tossed guess if its a head or a tail!! ")
guess=input("Enter your Guess: ").lower()

result=random.randint(1,10)
print(result)
if(result<6 and guess=="heads"):
    print("It was a head you won!!")
elif(result>5 and guess=="tails"):
    print("It was a tail you won!!")
else:
    print("You lost")
