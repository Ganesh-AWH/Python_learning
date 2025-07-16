import random
Friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_index = random.randint(0, 4)
print(f"{Friends[random_index]} should pay the bill")

#solution - 2
print(random.choice(Friends))