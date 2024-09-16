# ================= Problem Description =================
# This script calculates the square root of a user-provided number.
# 
# 1. Displays the program name.
# 2. Prompts the user to input a numerical value.
# 3. Computes the square root of the input value.
# 4. Displays the result.
#
# ================= Input =================
# - A numerical value (integer or floating-point) for which the square root is to be calculated.
#
# ================= Output =================
# - The square root of the input value.
#
# Example:
# Input:
# 16
#
# Output:
# Square Root : 4.0
# =========================================================

# ============= Solution 01 =============
# print("Program Name : Calculate Square Root")
# num = float(input("Enter a number :"))
# squareRoot = num**(1/2)
# print("Square Root : ", squareRoot)

# ============= Solution 02 =============
import math
print("Program Name : Calculate Square Root")
num = float(input("Enter a number :"))
squareRoot = math.sqrt(num)
print("Square Root : ", squareRoot)
