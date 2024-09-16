# ================= Problem Description =================
# This script calculates and displays the delivery time or date based on the order time.
# The delivery time is determined as follows:
# - If the order time is less than 6 hours, the delivery time is the current date.
# - If the order time is 6 hours or more, the delivery date is the following day.
# 
# 1. Prompts the user to input the order time in hours.
# 2. Calculates the delivery time or date based on the order time.
# 3. Displays the result.
# 4. Asks the user if they want to retry or quit.
#
# The program continues to prompt for new order times until the user decides to quit or provides invalid input.
#
# ================= Input =================
# - Order time (integer value representing hours).
#
# ================= Output =================
# - Delivery time or date based on the order time.
# - Option to retry or quit after each result.
#
# Example:
# Input:
# Enter order time: 3
# Output:
# Delivery time is: 2024-09-16
# Do you want to retry? (y/q): n
# =========================================================

from datetime import datetime, timedelta

# Get the current time without microseconds
current_date = datetime.now().strftime('%Y-%m-%d')
next_day_date = datetime.now().date() + timedelta(days=1)

def delivery_timer(order_time):
    if order_time < 6:
        print(f"Delivery time is: {current_date}")
    else:
        print(f"Delivery date is: {next_day_date}")

    retry = input("Do you want to retry? (y/q): ").lower()
    if retry != "y":
        quit()

while True:
    order_time = input("Enter order time (in hours): ")
    if order_time.isnumeric():
        order_time = int(order_time)
        delivery_timer(order_time)
    else:
        print("Not a valid input")
        retry = input("Do you want to retry? (y/q): ").lower()
        if retry != "y":
            break
