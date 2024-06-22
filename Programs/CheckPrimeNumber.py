print("Welcome to Prime Number Checking programme!")

run = True

def check_primenumber():
    num =  int(input("Enter number : "))
    
    if num == 1 :
        print(str(num) + " is not a prime number")
    
    else:
        for i in range(2, num):
            if num % i == 0 :
                print(str(num)+" is not a prime number fdg1")
                retry = input("Do you want to retry? (y/q): ").lower()
                if retry != "y":
                    run = False
                    quit()
                    
                else : 
                    break
            else : 
                print(str(num) + " is a prime number!  h")
                retry = input("Do you want to retry? (y/q): ").lower()
                if retry != "y":
                    run = False
                    quit() 
                else : 
                    break      
    
while run :
   
    check_primenumber()