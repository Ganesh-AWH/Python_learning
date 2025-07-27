#condtional statements
print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on you pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total_bill = 0

if(size == "S"):
    total_bill += 15;
    if(pepperoni == "Y"):
        total_bill += 2
    if(extra_cheese == "Y"):
        total_bill += 1
elif(size == "M"):
    total_bill +=20
    if(pepperoni == "Y"):
        total_bill += 3
    if(extra_cheese == "Y"):
        total_bill += 1
else:
    total_bill += 25
    if(pepperoni == "Y"):
        total_bill += 3
    if(extra_cheese == "Y"):
        total_bill += 1

print("total bill = " + str(total_bill))