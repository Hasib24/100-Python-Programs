# ================= Problem Description =================
# This script implements a simple computer quiz game.
# The user is prompted to play a quiz where they answer a question about computer hardware.
# 
# 1. Greets the user and asks if they want to play.
# 2. If the user responds with "yes", the quiz starts; otherwise, the program exits.
# 3. Asks the user a question about what CPU stands for.
# 4. Evaluates the user's answer and updates the score based on correctness.
# 5. Displays the final score and ends the quiz.
#
# ================= Input =================
# - User's response to the initial prompt ("yes" or any other response).
# - User's answer to the quiz question.
#
# ================= Output =================
# - Feedback on the correctness of the answer.
# - The final score after the quiz.
#
# Example:
# Input:
# Do you want to play? yes
# What does CPU stand for? central processing unit
# Output:
# Correct
# Your score is 1
# END
# =========================================================

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
else:
    print("Ok, let's play!")
    score = 0
    
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct") 
        score += 1
    else: 
        print("Incorrect")
    
    print(f"Your score is {score}")
    print("END")
