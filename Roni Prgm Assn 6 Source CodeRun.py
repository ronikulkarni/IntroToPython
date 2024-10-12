# Roni Kulkarni Programming Assignment 6 9-27-22

# This program determines batting average for 9 baseball players.

numBatter = 1
while numBatter < 10:
# Ask user to input number of hits and number of times at bat
    numBats = input("Please enter a number of times at bat ")
    numBats = int(numBats)
    numHits = input("Please enter a number of hits ")
    numHits = int(numHits)
    if numBats < 0 or numHits < 0:
        print("Please enter a positive number.")
    else:
        batAverage = float(numHits / numBats)
        batAverage = round(batAverage, 3)
        if batAverage > 0 and batAverage < 1:
            print("Player number " , numBatter, "Your number of hits is " , numHits, "Your number of times at bat is " , numBats, "The batting average is " , batAverage)
            numBatter = numBatter + 1
        else:
            print("Your batting average has to be between 0 and 1.")
        
    

