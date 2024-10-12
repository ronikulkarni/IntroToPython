# Roni Kulkarni Lab Assignment 13 10-20-22

# This program prints the speed of the driver and a warning using functions

# Define function to print the speed

def print_speed(speed) :
    print("You were driving at ", speed, " miles per hour.")

# Define function to print the warning
def print_warning() :
    print("**BE CAREFUL! YOU ARE DRIVING TOO FAST!**")

# Ask user to enter distance
distance = float(input("Please enter the distance you have driven in miles : "))

# Ask user to enter time taken
time = float(input("Please enter the time taken in hour : "))

# Calculate the speed and call function print speed
speed = distance / time
print_speed(speed)

# Check if speed is greater than 55 and print warning
if speed > 55:
    print_warning()

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni lab assn 13 code:output.py
Please enter the distance you have driven in miles : 112
Please enter the time taken in hour : 2
You were driving at  56.0  miles per hour.
**BE CAREFUL! YOU ARE DRIVING TOO FAST!**

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni lab assn 13 code:output.py
Please enter the distance you have driven in miles : 98
Please enter the time taken in hour : 2
You were driving at  49.0  miles per hour.
