import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissor = ''' _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
games_images = [rock, paper, scissor]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper and 2 for Scissors:\n"))

#print player game image
if(player_choice>=0 and player_choice<=2):
    print(f"player choice: \n {games_images[player_choice]}")


computer_choice = random.randint(0, 2)
print(f"Computer choice: \n{games_images[computer_choice]}")


#conditions
if(player_choice<0 or player_choice>=3):
    print("You type invalid number, You lose")

elif(player_choice == 0 and player_choice == 2):
    print("You win")
elif(player_choice == 2 and computer_choice == 0):
    print("You lose")
elif(player_choice > computer_choice):
    print("You win")
elif(player_choice < computer_choice):
    print("You lose")
else:
    print("Game Draw")
    