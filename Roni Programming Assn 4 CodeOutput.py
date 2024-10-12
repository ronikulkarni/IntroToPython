# Roni Kulkarni Programming Assn 4 9-15-22

# This program is a payroll program for a progressive company.

# Ask user to input if they are married or single
status = input("Please enter 0 if you are single or 1 if you are married ")
status = int(status)

if status == 0:
    hourlyrate = 10
elif status == 1:
    hourlyrate = 15
else:
    hourlyrate = 0
    
# Ask user to input number of children
numberofchildren = input("Please enter the number of children you have ")
numberofchildren = int(numberofchildren)

# a dollar extra for the first four children
if numberofchildren > 0 and numberofchildren <= 4:
    hourlyrate = hourlyrate + numberofchildren
elif numberofchildren > 4:
    hourlyrate = hourlyrate + 4

# Ask user for number of hours worked
numberofhours = input("Please enter the number of hours worked ")
numberofhours = int(numberofhours)

# extra hours is the hours worked greater than 40
regularhours = 40
if numberofhours > 40:
    extrahours = numberofhours - 40
else:
    extrahours = 0

# Calculate the gross pay
grosspay = hourlyrate * regularhours + (extrahours * 1.5 * hourlyrate)
print("The gross pay is " , grosspay)


OUTPUT

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni prgm assn 4 code.py
Please enter 0 if you are single or 1 if you are married 0
Please enter the number of children you have 0
Please enter the number of hours worked 40
The gross pay is  400.0

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni prgm assn 4 code.py
Please enter 0 if you are single or 1 if you are married 1
Please enter the number of children you have 2
Please enter the number of hours worked 40
The gross pay is  680.0

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni prgm assn 4 code.py
Please enter 0 if you are single or 1 if you are married 1
Please enter the number of children you have 6
Please enter the number of hours worked 40
The gross pay is  760.0

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni prgm assn 4 code.py
Please enter 0 if you are single or 1 if you are married 1
Please enter the number of children you have 8
Please enter the number of hours worked 50
The gross pay is  1045.0

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/Roni prgm assn 4 code.py
Please enter 0 if you are single or 1 if you are married 0
Please enter the number of children you have 0
Please enter the number of hours worked 75
The gross pay is  925.0

    
