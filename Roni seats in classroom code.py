# Roni Kulkarni Programming Assn 3 9-12-22

# This program determines the number of seats left in a classroom.

# Tell user to input number of students and total number  of seats in the classroom
numberofstudents = input(" Please enter the number of students in the classroom ")
numberofstudents = int(numberofstudents)


    

# Tell user to input total number of seats in the classroom
totalnumberofseats = input(" Please enter the total number of seats in the classroom ")
totalnumberofseats = int(totalnumberofseats)

if totalnumberofseats < 0:
    print("Please enter a non-negative integer for total number of seats")
elif numberofstudents < 0:
    print("Please enter a non-negative integer for number of students")
else:

    # Calculate number of seats left in the classroom
    numberofseatsleft = totalnumberofseats - numberofstudents

    if numberofseatsleft <= 0:
        print("There are no seats left in the class")
    else:
        print("There are " , numberofseatsleft, "seats left in the classroom")
