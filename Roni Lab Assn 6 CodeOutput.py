# Roni Kulkarni Lab Assignment #6 9-19-22

# This program prints numbers and their squares from 1 to n.

# Ask user to input any number n.

anynumber = input("Please enter any number ")
anynumber = int(anynumber)

if anynumber < 1:
    print("Please enter a number greater than 0")
else:
    for currentnumber in range (1, anynumber+1):
        print(currentnumber, " " , currentnumber ** 2)

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni Lab Assignment 6 9-19-22 Code.py
Please enter any number 1
1   1

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni Lab Assignment 6 9-19-22 Code.py
Please enter any number 2
1   1
2   4

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni Lab Assignment 6 9-19-22 Code.py
Please enter any number 3
1   1
2   4
3   9

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni Lab Assignment 6 9-19-22 Code.py
Please enter any number 4
1   1
2   4
3   9
4   16

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni Lab Assignment 6 9-19-22 Code.py
Please enter any number 5
1   1
2   4
3   9
4   16
5   25
