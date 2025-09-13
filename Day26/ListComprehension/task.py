with open(r"Day26\Task\file1.txt") as file1:
    list1 = file1.readlines()

with open(r"Day26\Task\file2.txt") as file2:
    list2 = file2.readlines()
    

file1_numbers = [int(item.strip()) for item in list1]
file2_numbers = [int(item.strip()) for item in list2]


result = [item for item in file1_numbers if item in file2_numbers]

print(result)