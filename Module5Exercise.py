"""
import random
def roll_dice(num_dice):
    total_sum = 0
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        total_sum += roll
        print(f"Roll {_ + 1}: {roll}")
    return total_sum
num_dice = int(input("How many times shall the dice roll? "))
if num_dice <= 0:
    print("Enter a positive integer for the number of dice.")
else:
    sum_of_rolls = roll_dice(num_dice)
    print(f"Sum of all rolls: {sum_of_rolls}")
"""
"""
Numbers = []
while True:
    User_input = input("Enter a number or press (Enter) to quit: ")
    if User_input == "":
        break
    try:
        Number = float(User_input)
        Numbers.append(Number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
if not Numbers:
    print("You did not enter any numbers.")
else:
    Numbers.sort(reverse=True)
    topfive = Numbers[:5]
    print("The five greatest numbers in descending order are:")
    for i, num in enumerate(topfive, 1):
        print(f"{i}. {num}")
"""
"""
import math
def is_prime(Num):
    if Num <= 1:
        return False
    if Num <= 3:
        return True

    if Num % 2 == 0 or Num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(Num)) + 1, 6):
        if Num % i == 0 or Num % (i + 2) == 0:
            return False
    return True
try:
    Num = int(input("Enter integer: "))
    if is_prime(Num):
        print(f"{Num} is in fact a prime number.")
    else:
        print(f"{Num} is actually not a prime number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
"""
"""
Cities = []
for i in range(5):
    Cityname = input(f"Enter City name {i + 1}: ")
    Cities.append(Cityname)
print("The names of the cities are: ")
for City in Cities:
    print(City)
"""

