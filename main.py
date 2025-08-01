#!/usr/bin/env python3
"""
Main entry point for the Python application.
"""

def greet_user(name):
    """Greet the user with a personalized message."""
    return f"Hello, {name}! Welcome to your Python workspace!"

def calculate_square(number):
    """Calculate the square of a number."""
    return number ** 2

def minus_five(number):
    """Subtract 5 from a number."""
    return number - 5

def main():
    """Main function that runs when the script is executed."""
    print("Hello, World! Welcome to your Python workspace!")
    print("You can start coding here!")
    print ("This is a test change")
    print ("This is a test change 2")
    
    # Example: Add your code here
    name = input("What's your name? ")
    print(greet_user(name))
    
    # New feature: Calculate square
    try:
        number = int(input("Enter a number to square: "))
        result = calculate_square(number)
        print(f"The square of {number} is {result}")
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main() 