"""
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1
"""
"""
inchestocm = 2.54
while True:
    inches = int(input("Enter length in inches (Enter negative value to exit): "))
    if inches < 0:
        print("Exit the program.")
        break
    cm = inches * inchestocm
    print(f"{inches} inches is equal to {cm:.2f} centimeters")
"""
"""
#Write a program that asks the user to enter numbers until they enter an empty string to quit.
numbers = []
while True:
    userinput = input("Enter a number or press *Enter* to quit: ")
    if userinput == "":
        break
#Write a program that prints out the smallest and largest number from the numbers it received.
numbers = [userinput]
smallest = min(numbers)
largest = max(numbers)
print(f"Largest: {largest}. Smallest: {smallest}")
"""
"""
import random
#Write a game where the computer draws a random integer between 1 and 10:
random_number = random.randint(1,10)
attempts = 0
#Ask the user to guess number:
while True:
    user_input = int(input("Guess the number :"))
    attempts += 1
    break
if user_input == random_number:
    print("COREECT.")
if user_input > random_number:
     print("WRONG, too HIGH!!")
if user_input < random_number:
    print("WRONG, too LOW!")
"""
"""
Username = "Fadak"
Password = "1999"
max_attempts = 5
attempts = 0
while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == Username and password == Password:
        print("Welcome back!")
        break
    else:
        print("Incorrect username or password. Please try again.")
        attempts += 1
if attempts == max_attempts:
    print("Access denied")
"""




