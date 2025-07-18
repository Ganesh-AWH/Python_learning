import random

#hang man stages
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
hang_length = len(HANGMANPICS)

print("Welcome to Hangman Game!")
print(''' 
            _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
 jgs_|___
''')

#Getting random a word from list
words_list = ["apple", "ball", "cat", "dog", "camel"]
word_index = random.randint(0, len(words_list)-1)

random_word = words_list[word_index]
print(random_word)


#setting place holder
place_holder = ""
word_length = len(random_word)
for i in range(word_length):
    place_holder += "-"
print(f"Word to Guess: {place_holder}")

#updating the place holder
correct_letters = []

game_over = False
total_lives = 7
lives = total_lives
while not game_over:
    #get the letter from user and check with random word
    guess_letter = input("Guess a letter: ").lower()

    #displaying the guessed letters
    display = ""
    found_correct = False
    for letter in random_word:
        
        if letter == guess_letter:
            display += letter
            correct_letters.append(guess_letter)
            found_correct = True
    
        elif letter in correct_letters:
            display += letter
        
        else:
            display += "-"
    
    if(not found_correct):
        lives -= 1
    
    
    
    if '-' not in display:
        game_over = True
        print("You won")
    
    if lives <= 0:
        game_over = True
        print("*******************You are out of lives and You lose!*******************")
        print("Game over")
        break
    
    print(f"Guessed letters: {display}")
    print(HANGMANPICS[hang_length - lives])
        
    print(f"*******************number of lives remaining: {lives}/{total_lives}*******************")