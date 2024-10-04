
def calculate_factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        print(i)
    return factorial

def main():
    while True:
        try:
            digit = input("Enter a non-negative integer to calculate its factorial: ")
            digit = int(digit)
            if digit < 0:
                raise ValueError("The number must be non-negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    result = calculate_factorial(digit)
    print(f"The factorial of {digit} is {result}")

if __name__ == "__main__":
    main()