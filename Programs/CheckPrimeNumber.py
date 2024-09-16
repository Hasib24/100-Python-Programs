# ================= Problem Description =================
# This script determines whether a given number is a prime number.
# A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
# 
# 1. Displays a welcome message.
# 2. Prompts the user to input a number.
# 3. Checks if the entered number is a prime number.
# 4. Displays whether the number is prime or not.
# 5. Asks the user if they want to retry or quit.
#
# The program continues to prompt for new numbers until the user decides to quit.
#
# ================= Input =================
# - A number (integer value).
#
# ================= Output =================
# - A message indicating whether the number is a prime number or not.
# - Option to retry or quit after each result.
#
# Example:
# Input:
# Enter number: 7
# Output:
# 7 is a prime number!
# Do you want to retry? (y/q): n
# =========================================================

print("Welcome to Prime Number Checking programme!")

def check_prime_number():
    num = int(input("Enter number: "))
    
    if num < 2:
        print(f"{num} is not a prime number")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number")
                retry = input("Do you want to retry? (y/q): ").lower()
                if retry != "y":
                    quit()
                return
        print(f"{num} is a prime number!")
    
    retry = input("Do you want to retry? (y/q): ").lower()
    if retry != "y":
        quit()

while True:
    check_prime_number()
