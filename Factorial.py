def calculate_factorial(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial

try:
    user_input = int(input("Enter an integer: "))
    if user_input < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = calculate_factorial(user_input)
        print(f"The factorial of {user_input} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

