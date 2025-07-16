#Tip calculator
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? Rs: "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
no_of_people = int(input("How many people to split the bill? "))

total_amount = total_bill + (tip/100 * total_bill)
split = round(total_amount/no_of_people, 2);
print(f"Each person should pay: Rs {split}")