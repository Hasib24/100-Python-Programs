print("Welcome to Leap Year programme!")

def check_leap_year(y):
    if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
        print(str(y) + " is a leap year !")
        retry = input("Do you want to retry? (y/q): ").lower()
        if retry != "y":
            quit()
    else:
        print(str(y) + " is not a leap year")
        retry = input("Do you want to retry? (y/q): ").lower()
        if retry != "y":
            quit()

while True:
    y = input("Enter year : ")
    if y.isnumeric():
        y = int(y)
        check_leap_year(y)
    else:
        print("Not a valid input")
        retry = input("Do you want to retry? (y/q): ").lower()
        if retry != "y":
            break
