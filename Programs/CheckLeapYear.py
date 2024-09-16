# ================= Problem Description =================
# This script determines whether a given year is a leap year.
# It prompts the user to enter a year and checks if it is a leap year based on the following criteria:
# - A year is a leap year if it is divisible by 4 and not divisible by 100, or if it is divisible by 400.
# 
# 1. Displays a welcome message.
# 2. Prompts the user to input a year.
# 3. Checks if the entered year is a leap year.
# 4. Displays whether the year is a leap year or not.
# 5. Asks the user if they want to retry or quit.
#
# The program continues to prompt for a new year until the user decides to quit or provides invalid input.
#
# ================= Input =================
# - A year (integer value).
#
# ================= Output =================
# - A message indicating whether the year is a leap year or not.
# - Option to retry or quit after each result.
#
# Example:
# Input:
# Enter year: 2024
# Output:
# 2024 is a leap year!
# Do you want to retry? (y/q): n
# =========================================================

print("Welcome to Leap Year programme!")

def check_leap_year(y):
    if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
        print(f"{y} is a leap year!")
    else:
        print(f"{y} is not a leap year")
    retry = input("Do you want to retry? (y/q): ").lower()
    if retry != "y":
        quit()

while True:
    y = input("Enter year: ")
    if y.isnumeric():
        y = int(y)
        check_leap_year(y)
    else:
        print("Not a valid input")
        retry = input("Do you want to retry? (y/q): ").lower()
        if retry != "y":
            break
