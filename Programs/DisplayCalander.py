import calendar
from colorama import Fore, Style
from utils.terminal_utils import clear_terminal

clear_terminal()
print(f"{Fore.GREEN}Welcome to Display Calendar Program{Style.RESET_ALL}")


# Function to get valid year input
def get_year():
    while True:
        try:
            year = int(input("Enter year: "))
            return year
        except ValueError:
            print(
                f"{Fore.RED}Invalid input! Please enter a valid year (numbers only).{Style.RESET_ALL}"
            )
            retry = input("Do you want to retry ? (y/q) : ").lower()
            if retry != "y":
                quit()


# Function to get valid month input
def get_month():
    while True:
        try:
            month = int(input("Enter month (1-12): "))
            if 1 <= month <= 12:
                return month
            else:
                print(
                    f"{Fore.RED}Invalid input! Please enter a month between 1 and 12.{Style.RESET_ALL}"
                )
        except ValueError:
            print(
                f"{Fore.RED}Invalid input! Please enter a valid month (numbers only).{Style.RESET_ALL}"
            )
            retry = input("Do you want to retry ? (y/q) : ").lower()
            if retry != "y":
                quit()


# Generate and display the calendar
def generate_and_display_calander():
    # Get valid inputs
    year = get_year()
    month = get_month()
    clear_terminal()
    cal = calendar.month(year, month)
    print(cal)


try:
    while True:
        generate_and_display_calander()
        retry = input("Do you want to retry ? (y/q) : ").lower()
        if retry != "y":
            quit()

except KeyboardInterrupt:
    print(
        f"\n {Fore.YELLOW} Program interrupted. {Fore.GREEN}Exiting gracefully...{Style.RESET_ALL}"
    )
