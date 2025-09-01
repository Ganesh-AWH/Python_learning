def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1-n2
def mul(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1//n2

def calculator(n1, n2, func):
    return func(n1, n2)
    
n1 = 10
n2 = 30

#add is the function that has been passed as a parameter
ans = calculator(n1, n2, add)
print(ans)