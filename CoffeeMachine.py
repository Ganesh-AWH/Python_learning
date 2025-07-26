MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 12,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_resources():
    print("Water: ", resources["water"])
    print("Milk: ", resources["milk"])
    print("Coffee: ", resources["coffee"])
    print(f"Money: {profit} Rs")

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there in not enough {item} for your drink")
            return False
    return True

def process_coins(drink):
    #get coins from user 
    amount = int(input(f'enter {drink["cost"]} Rs to enjoy your drink: '))
    #check sufficient amount
    if(amount < drink["cost"]):
        print("You don't have enough amount, amount refunded")
    else:
        global profit
        profit += drink["cost"]
        change = amount - drink["cost"]
        if(change > 0):
            print(f"Here is the remaing change of {change} Rs")
        print("Amount has been processed, Wait for Sometime Your drink is been preparing")
        
def make_coffee(order_ingredients):
    for item in order_ingredients:
        resources[item] = resources[item] - order_ingredients[item]
    
#variables declaration and initialization
is_on = True
profit = 0
list_commands = ["espresso", "latte",  "cappuccino", "report", "off"]
while is_on:
    #asking user to get input
    choice =  input("What would you like? (espresso/latte/cappuccino/report): ").lower()
    if(choice not in list_commands):
        print("Invalid command") 
    elif choice == "off":
        is_on = False
    #print report
    elif(choice == "report"):
        print_resources()

    #check resoureces
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            process_coins(drink)
            make_coffee(drink["ingredients"])
            print(f"Here is your {choice} ☕, Enjoy your drink")
            print("Visit Again ")


