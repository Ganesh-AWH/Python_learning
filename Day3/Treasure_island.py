#use ascii art for this below art work and triple quote is for to print multiple lines
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 
''')

print("Welcome to treasure island your mission is to find the treasure.")
print("You are at cross road. Where do you want to go?")
direction  = input("Type left or right\n")

direction = direction.lower()
if(direction == "left"):
    
    print("You have come to lake. There is an island in the middle of the lake.")
    decision = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    decision = decision.lower()
    
    if(decision == "wait"):
    
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        color = input("One red, one Yellow and one blue. Which color do you choose? \n")
        color = color.lower()
        if(color == "yellow"):
            print("You won")
        elif(color == "red"):
            print("Room is full of fire Game over")
        elif(color == "blue"):
            print("Room is full of bees")
    else:
        print("You got attacked by angry trout. Game over")
else:
    print("You fell into a hole Game Over")