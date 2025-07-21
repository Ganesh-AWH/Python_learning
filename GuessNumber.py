import random
print('''

  /$$$$$$                                               /$$   /$$                         /$$                          
 /$$__  $$                                             | $$$ | $$                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$      | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$       | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/       |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      
            
''')

print("Welcome to the number Guessing game!")
print("I'm thinking of number between 1 to 100.")
guess_number = random.randint(1, 100)

attempts = 0
difficulty_level = input("Choose a difficulyt level. Type 'easy' or 'hard': ")
if(difficulty_level == 'easy'):
    attempts = 10
else:
    attempts = 5

game_over = False
while(not game_over):
    print(f"You have {attempts} attempts remaining to guess the number")
    user_guess = int(input("Make a guess: "))
    if(user_guess > guess_number):
        print("Too high.")
        print("Guess again")
        attempts -= 1
    elif(user_guess < guess_number):
        print("Too low.")
        print("Guess again")
        attempts -= 1
    else:
        print(f"You got it! The answer was {guess_number}")
        game_over = True

    if(attempts <= 0):
        print("You are out of attempts, You lose")
        game_over = True
