"""
import random
def diceroll():
    return random.randint(1, 6)
def main():
    rollcounts = 0
    while True:
        rollresults = diceroll()
        rollcounts += 1
        print(f"Roll {rollcounts}: {rollresults}")
        if rollresults == 6:
            break
if __name__ == "__main__":
    main()
"""
"""
def gal_to_l(gal):
    l = gal * 3.78541
    return l
def main():
    while True:
        gal = float(input("Enter the volume in American gallons or a negative value to quit: "))
        if gal < 0:
            break
        l = gal_to_l(gal)
        print(f"{gal} American gallons is approximately {l} liters.")
if __name__ == "__main__":
    main()
"""
"""
def listsum(Numbers):
    Total = sum(Numbers)
    return Total
def main():
    integerlist = [1, 2, 3, 4, 5]
    results = listsum(integerlist)
    print("Sum of the list:", results)
if __name__ == "__main__":
    main()
"""
"""
def RemoveOddNumbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers
def main():
    ListOfIntegers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    EvenList = RemoveOddNumbers(ListOfIntegers)

    print("The original list:", ListOfIntegers)
    print("The cut-down list (Even numbers):", EvenList)
if __name__ == "__main__":
    main()
"""
"""
import math
def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius**2)
    unit_price = price / (area / 10_000)
    return unit_price
def main():
    diameter1 = float(input("Enter the diameter of the first pizza (in cm): "))
    price1 = float(input("Enter the price of the first pizza (in euros): "))
    diameter2 = float(input("Enter the diameter of the second pizza (in cm): "))
    price2 = float(input("Enter the price of the second pizza (in euros): "))
    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)
    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas have the same unit price.")
if __name__ == "__main__":
    main()
"""
