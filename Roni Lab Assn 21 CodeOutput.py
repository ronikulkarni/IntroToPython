# Roni Kulkarni Lab Assn 21 11-21-22

# This program prints an output of list functions and operations

# Declare variables mylist and yourlist and print
mylist = [4, 2, [5, 6, 37], 13, 13, 29]
print(mylist)
yourlist = ["socks", "pillowcases", "tablecloth", 34.5]
print(yourlist)

# Print these options
print("mylist length", len(mylist))
print("mylist maximum", max(mylist[2]))
print("mylist minimum", min(mylist[2]))
print("second item in mylist", mylist[2][2])
print("sum in mylist", sum(mylist[2]))
print("first item in yourlist", yourlist[-2:])
print("second item in yourlist", yourlist[0])
print("'socks' in yourlist", "socks" in yourlist)
print("product of yourlist and 3", yourlist*3)
print("yourlist is less than socks and pillows", yourlist < ["socks", "pillows"])

= RESTART: /Users/rohan/Documents/roni/Adelphi Fall 2022/Intro To Python/roni lab assn 21 code.py
[4, 2, [5, 6, 37], 13, 13, 29]
['socks', 'pillowcases', 'tablecloth', 34.5]
mylist length 6
mylist maximum 37
mylist minimum 5
second item in mylist 37
sum in mylist 48
first item in yourlist ['tablecloth', 34.5]
second item in yourlist socks
'socks' in yourlist True
product of yourlist and 3 ['socks', 'pillowcases', 'tablecloth', 34.5, 'socks', 'pillowcases', 'tablecloth', 34.5, 'socks', 'pillowcases', 'tablecloth', 34.5]
yourlist is less than socks and pillows True

                                        
