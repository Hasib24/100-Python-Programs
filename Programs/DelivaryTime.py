This problem was descrived by [] 

from datetime import datetime, timedelta

# Get the current time without microseconds
current_date = datetime.now().strftime('%Y-%m-%d')
next_day_date = datetime.now().date() + timedelta(days=1)




def deliveryTimer (orderTime):
    if orderTime < 6 :
        print("Delivary time is : " + current_date)
        
        retry = input("Do you want to retry? (y/q): ").lower()
        if retry != "y":
            quit()
    else:
        print("Delivary date is : " + str(next_day_date))
        
        retry = input("Do you want to retry? (y/q): ").lower()
        if retry != "y":
            quit()




while True:
    orderTime = input("Enter order time : ")
    if orderTime.isnumeric():
        orderTime = int(orderTime)
        deliveryTimer(orderTime)
    else:
        print("Not a valid input")
        retry = input("Do you want to retry? (y/q): ").lower()
        if retry != "y":
            break

