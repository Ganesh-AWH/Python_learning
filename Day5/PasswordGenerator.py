import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to  PyPassword generator!")
no_letters = int(input("How many letters would you like in password\n"))
no_symbols = int(input("How many symbols would you like?\n"))
no_numbers = int(input("How many number would you like?\n"))

version1 = []

# Easy soltion

#first random letters
while(True):
    random_index = random.randint(0, len(letters)-1)
    if(letters[random_index] not in version1):
        version1.append(letters[random_index])
    if(len(version1)==no_letters):
        break

#second random symbols
while(True):
    random_index = random.randint(0, len(symbols)-1)
    if(symbols[random_index] not in version1):
        version1.append(symbols[random_index])
    if(len(version1) == no_symbols+no_letters):
        break
    
#third rand numbers
while(True):
    random_index = random.randint(0, len(numbers)-1)
    if(numbers[random_index] not in version1):
        version1.append(numbers[random_index])
    if(len(version1) == no_symbols+no_letters+no_numbers):
        break

print(version1)    

#Hard solution
version2 = []

while(True):
    random_index = random.randint(0, len(version1)-1)
    if(version1[random_index] not in version2):
        version2.append(version1[random_index])
    if(len(version1) == len(version2)):
        break
print(version2)

password = ""

for i in version2:
    password += i
print(f"Your strongest pasword is {password}")