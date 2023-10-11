"""
def get_season(month_number):
    seasons = ("Winter", "Spring", "Summer", "Autumn")
    season_boundaries = (0, 2, 5, 8)
    for i in range(len(seasons)):
        if season_boundaries[i] <= month_number <= season_boundaries[i + 1]:
            return seasons[i]
    return "Invalid month"
def main():
    month_number = int(input("Enter a month number (1-12): "))
    if 1 <= month_number <= 12:
        season = get_season(month_number - 1)  # Adjust month_number to be 0-based
        print(f"The season for month {month_number} is {season}.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
if __name__ == "__main__":
    main()
"""
"""
names_set = set()
input_names = []
while True:
    name = input("Enter a name (or press Enter to finish): ")
    if not name:
        break
    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        names_set.add(name)
    input_names.append(name)
print("\nList of input names:")
for name in input_names:
    print(name)
"""
