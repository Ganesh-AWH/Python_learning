#import all libraries and datas
from art import logo, vs
from gamedata import data
import random

#Functions Definitions
def Format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def Compare_accounts(account_a, account_b):
    a_followers  = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    if(a_followers > b_followers):
        return 'a'
    else:
        return 'b'   

score = 0
game_over = False

#print the logo
print(logo)

while(not game_over):
    #Get two random account 
    account_a = random.choice(data)
    account_b = random.choice(data)
    if(account_a == account_b):
        account_b = random.choice(data)


    #format the data and print it
    print(Format_data(account_a))
    #print logo of VS
    print(vs)
    print(Format_data(account_b))

    # ask user to guess accounts like 'A' or 'B'
    user_guess = input("Who has more followers? 'A' or 'B': ").lower()

    #compare the accounts 
    winner = Compare_accounts(account_a, account_b)
    
    #give the feedback for the guess 
    if(winner == user_guess):
        score += 1
        print(logo)
        print(f"You're right! Current score: {score}")
    else:
        print(logo)
        print(f"Sorry that's wrong. Final score: {score}")
        game_over = True