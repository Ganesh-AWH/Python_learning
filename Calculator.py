def add(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1/num2

print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

num1 = float(input("What is the first number: "))
program_end = False
while not program_end:
    print("+\n-\n*\n/")
    operation = input("Enter the option: ")
    num2 = float(input("What's the next number: "))
    if(operation == '+'):
        num1 = add(num1, num2)
    elif(operation == '-'):
        num1 = sub(num1, num2)
    elif(operation == '*'):
        num1 = mul(num1, num2)
    elif(operation == '/'):
        num1 = div(num1, num2)
    else:
        print("Invalid operation enter valid operation show above")
        continue
    print(f"Result = {num1}")
    option = input("Press 'y' to continue and 'n' to Quit program: ")
    if(option == 'n'):
        program_end = True
    