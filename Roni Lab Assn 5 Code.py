# Roni Kulkarni Lab Assignment #5

# This program determines tax rate based on weekly salary.

weeklysalary = input(" Please enter your weekly salary ")
weeklysalary = int(weeklysalary)

if weeklysalary >= 1000:
    print("Your tax rate is 8%")
    taxrate = 8
elif weeklysalary >= 600:
    print("Your tax rate is 6%")
    taxrate = 6
elif weeklysalary >= 400:
    print("Your tax rate is 4%")
    taxrate = 4
else:
    print("Your tax rate is 0%")
    taxrate = 0

totaltax = weeklysalary * (taxrate/100)
print("Your total tax is " , totaltax)
