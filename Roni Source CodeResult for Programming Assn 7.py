# Roni Kulkarni Programming Assignment 7 9-30-22

negativeInput = True

while negativeInput:
    # Ask user to input number of dependents
    numDependents = input("Please enter the number of dependents ")
    numDependents = int(numDependents)
    
    # Ask user for number of hours worked
    numberofhours = input("Please enter the number of hours worked ")
    numberofhours = int(numberofhours)
    if numberofhours < 0 or numDependents < 0:
        print("Please enter a positive number for number of hours and number of dependents")
    else:
        negativeInput = False
        # extra hours is the hours worked greater than 40
        hourlyrate = 16.78
        regularhours = 0
        if numberofhours > 40:
            regularhours = 40
            extrahours = numberofhours - regularhours
        else:
            extrahours = 0
            regularhours = numberofhours
        # Calculate the gross pay
        healthinsurance = 0
        grosspay = hourlyrate * regularhours + (extrahours * 1.5 * hourlyrate)
        socialSecTax = (6 / 100) * grosspay
        fedIncomeTax = (14 / 100) * grosspay
        stateIncomeTax = (5 / 100) * grosspay
        unionDues = 10
        if numDependents >= 3:
            healthinsurance = 35
        netpay = grosspay - socialSecTax - fedIncomeTax - stateIncomeTax - unionDues - healthinsurance
        print("Your gross pay is: " , round(grosspay, 2))
        print("Your social security tax is: " , round(socialSecTax, 2))
        print("Your federal income tax is: " , round(fedIncomeTax, 2))
        print("Your state income tax is: " , round(stateIncomeTax, 2))
        print("Your union dues are: " , unionDues)
        print("Your health insurance deduction is: " , healthinsurance)
        print("Your net pay is: " , round(netpay, 2))

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/roni prgm assn 7.py
Please enter the number of dependents 4
Please enter the number of hours worked 50
Your gross pay is:  922.9
Your social security tax is:  55.37
Your federal income tax is:  129.21
Your state income tax is:  46.15
Your union dues are:  10
Your health insurance deduction is:  35
Your net pay is:  647.18

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/roni prgm assn 7.py
Please enter the number of dependents 0
Please enter the number of hours worked 60
Your gross pay is:  1174.6
Your social security tax is:  70.48
Your federal income tax is:  164.44
Your state income tax is:  58.73
Your union dues are:  10
Your health insurance deduction is:  0
Your net pay is:  870.95

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/roni prgm assn 7.py
Please enter the number of dependents -1
Please enter the number of hours worked -10
Please enter a positive number for number of hours and number of dependents
Please enter the number of dependents -1
Please enter the number of hours worked 5
Please enter a positive number for number of hours and number of dependents
Please enter the number of dependents 2
Please enter the number of hours worked 40
Your gross pay is:  671.2
Your social security tax is:  40.27
Your federal income tax is:  93.97
Your state income tax is:  33.56
Your union dues are:  10
Your health insurance deduction is:  0
Your net pay is:  493.4
