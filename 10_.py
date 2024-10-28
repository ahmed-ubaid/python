#BILL SPLITTER
totalBill=input("How much is the total bill? ")
totalBillInt=int(totalBill)
num_of_ppl=input("How many people are there? ")
numInt=int(num_of_ppl)
tip_per=input("What is the percentage of tip? ")
tipInt=int(tip_per)
total=round((totalBillInt+(totalBillInt*(tipInt/100))),1)
split_per_person=round((total/numInt),1)
print(f"Your total will be {total}. Each person in entitlied to pay {split_per_person}")



