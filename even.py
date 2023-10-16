# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get user input
user_number = int(input("Enter a number: "))

# Call the function and display the result
result = check_even_odd(user_number)
print(f"The number {user_number} is {result}.")
