from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print('''
              ..
      ..  ..
            ..
             ..
            ..
           ..
         ..
##       ..    ####
##.............##  ##
##.............##   ##
##.............## ##
##.............###
 ##...........##
  #############
  #############
#################
-Berry-
''')


is_on = True
#the list of commands that are valid
list_commands = ["espresso", "latte", "cappuccino", "report", "off"]

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    user_choice = input(f"What would you like? {menu.get_items()}: ").lower()
    
    if(user_choice not in list_commands):
        print("Invalid command, Type valid commands")
        
    elif user_choice == "off":
        print("Machine is turned off")
        is_on = False
    
    elif user_choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if(coffe_maker.is_resource_sufficient(drink)):
            cost = money_machine.process_coins()
            if(money_machine.make_payment(cost)):
                coffe_maker.make_coffee(drink)
        