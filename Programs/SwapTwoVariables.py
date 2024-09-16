# ================= Problem Description =================
# This script demonstrates two methods for swapping the values of two variables and checks if a number is even or odd.
#
# 1. **Variable Swapping**: 
#    - Solution 01 swaps the values of two variables using a temporary variable.
#    - Solution 02 swaps the values of two variables using tuple unpacking.
# 2. **Number Check**:
#    - Checks if a predefined number is even or odd and prints the result.
#
# ================= Input =================
# - No user input is required for variable swapping.
# - A predefined number is used for checking even or odd.
#
# ================= Output =================
# - Displays the swapped values of the variables.
# - Displays whether the predefined number is even or odd.
#
# Example:
# Output for variable swapping:
# x is 7 y is 5
#
# Output for number check:
# Odd number
# =========================================================

# ============= Solution 01 =============
# x = 5
# y = 7
# temp = x
# x = y
# y = temp
# print("x is ", x, "y is ", y)

# ============= Solution 02 =============
x = 5
y = 7
x, y = y, x

print("x is", x, "y is", y)

number = 11
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
