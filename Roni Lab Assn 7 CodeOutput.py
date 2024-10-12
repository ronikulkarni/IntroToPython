# Roni Kulkarni Lab Assignment 7 9-20-22

# This program prints the tax rate for married or single user n number of times

# Ask user to input any number n
num = input("Please enter any number n ")
num = int(num)

if num <= 0:
    print("Please print a number greater than 0")
else:
    for x in range (num):
        status = input("Please enter 1 for married or 0 for single ")
        status = int(status)
        if status == 0:
            print("Your tax rate is 35%")
        elif status == 1:
            print("Your tax rate is 32%")
        else:
            print("Please enter 0 or 1")
            break

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni Lab Assn 7 Code.py
Please enter any number n -1
Please print a number greater than 0

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni Lab Assn 7 Code.py
Please enter any number n 0
Please print a number greater than 0

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni Lab Assn 7 Code.py
Please enter any number n 1
Please enter 1 for married or 0 for single 0
Your tax rate is 35%

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni Lab Assn 7 Code.py
Please enter any number n 3
Please enter 1 for married or 0 for single 1
Your tax rate is 32%
Please enter 1 for married or 0 for single 0
Your tax rate is 35%
Please enter 1 for married or 0 for single 1
Your tax rate is 32%

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni Lab Assn 7 Code.py
Please enter any number n 2
Please enter 1 for married or 0 for single -1
Please enter 0 or 1
