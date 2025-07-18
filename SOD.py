num = 567 
sum = 0
while num > 0:
    sum = sum + (num % 10)
    # print(num)
    num = num // 10
    print(num)
print(sum)