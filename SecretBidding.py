print('''
      
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\
''')
print("Welcome to secret bidding!")

is_bidders_present = True
bids = {}
while is_bidders_present:
    
    bidder_name = input("What is you name: ")
    bid_value = int(input("What is your bid: "))
    bids[bidder_name] = bid_value 
    option = input("Are any other bidders? Type 'Yes' or 'No': ").lower()
    
    if(option == "no"):
        is_bidders_present = False
    
    #print result of the bids
    print("\n" * 100)
    

#Displaying the winner of the bids
max = 0
winner = None 
for bidders, values in bids.items():
    if max < values:
        winner = bidders
        max = values

print(f"The winner is {winner} of bid value {max}")
