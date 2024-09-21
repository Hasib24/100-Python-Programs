# ================= Problem Description =================
# This program takes a single character as input from the user and returns its corresponding ASCII value.
#
# ================= Input =================
# - A single character provided by the user.
#
# ================= Output =================
# - The ASCII value of the entered character.
#
# ================= Example =================
# Example 1:
# Input: 'A'
# Output: The ASCII value of A is 65
#
# Example 2:
# Input: 'b'
# Output: The ASCII value of b is 98
# =========================================================
import os
from colorama import Fore, Style

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
clear_terminal() 

print(f"{Fore.GREEN}Welcome to ASCII Value Find program{Style.RESET_ALL}")

def find_ASCII_value():
    char = input("Enter any character: ")
    if len(char) > 1:
        print(f"\n{Fore.RED}Sorry!, you can not enter more than one character at a time {Style.RESET_ALL}")
        retry = input("Do you want to retry ? (y/q) : ").lower()
        if retry != "y":
            quit()
    else:
        print(f"\n{Fore.GREEN}The ASCII value of '{char}' is: {Fore.YELLOW}{ord(char)}{Style.RESET_ALL}")
        retry = input("Do you want to retry ? (y/q) : ").lower()
        if retry != "y":
            quit()

try:
    while True:
        find_ASCII_value()
except KeyboardInterrupt:
    print(f"\n {Fore.YELLOW} Program interrupted. {Fore.GREEN}Exiting gracefully...{Style.RESET_ALL}")

