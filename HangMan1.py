import random
#randomly a word from list
words_list = ["apple", "ball", "cat", "dog", "camel"]
word_index = random.randint(0, len(words_list)-1)

random_word = words_list[word_index]
print(random_word)

#get the letter from user and check with random word
guess_letter = input("Guess the letter: ")

list_char = list(random_word)

for i in list_char:
    if i == guess_letter:
        print("Right")
    else:
        print("Wrong")