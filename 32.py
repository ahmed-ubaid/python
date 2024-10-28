import os

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux (os.name is 'posix')
    else:
        os.system('clear')

# Example usage:
auction_list={}

playing=True
maxBid=0
winner=''

while(playing):

    name=input("Enter your name: ")
    bid=int(input("Enter your bid: "))

    auction_list.update({name:bid})

    if(bid>maxBid):
        maxBid=bid
        winner=name

    playing=True if input("Are there any more bidder 'Yes' or 'No':").strip().lower()=='yes' else False 

    clear_terminal()

print(f"The winner is {winner} with the bid of {auction_list[winner]}")

