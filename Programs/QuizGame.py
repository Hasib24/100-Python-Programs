print("Welcome to my computer quize!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
else:
    print("Ok, let's play!")
    score = 0
    
answer = input("What dose CPU stand for? ")
if answer.lower() == "central processing unit" :
    print("Correct") 
    score += 1
else: 
    print("Incorrct")
    
    
print("Your score is " + str(score))
print("END")