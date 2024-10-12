############################################################################
# This program encrypts and decrypts text using different methods
# Authors : Roni Kulkarni, Hugo Ledesma, John Lund, Nikita Korzhenko
#
# Version :     1.0 on 05/11/2024 encrypt/decrypt using random shuffle key
#               2.0 on 05/12/2024 encrypt/decrypt using function(commented out)
#               3.0 on 05/12/2024 added functionality with loops
#
#############################################################################

# import the required modules
import string
import random
import math

# get all characters in a list
allCharacters = string.ascii_letters + string.punctuation + string.digits + " "
listOfChars = list(allCharacters)

# make a copy of the list of characters and shuffle them to get the key
shuffledKeys = listOfChars.copy()
random.shuffle(shuffledKeys)

# Define function to encrypt a string
def randomkeyEncrypt(simpleText) :
    encryptedText = ""

    # loop through each character in simpletext and replace it by a character from shuffledKeys at the same index
    for aChar in simpleText :
        listIndex = listOfChars.index(aChar)
        encryptedText += shuffledKeys[listIndex]

    return encryptedText

# Define function to decrypt a string
def randomkeyDecrypt(encryptedText) :
    decryptedText = ""
     # loop through each character in encryptedText and replace it by the original character
    for aChar in encryptedText :
        listIndex = shuffledKeys.index(aChar)
        decryptedText += listOfChars[listIndex]

    return decryptedText

#Only contains capital letters
formulaLetters = listOfChars[26:52]

#Encrypts messages exactly how we did in class
def encryptWithFormula(formula, message):
  formula = formula.replace(" ","")[formula.index("="):]
  try:
    a = int(formula[formula.index("(")+1:formula.index("x")])
  except:
    a = 1
  try:
    b = int(formula[formula.index("x")+1:formula.index(")")])
  except:
    b = 0
  encryptedMessage = ""
  for i in message:
    pos = formulaLetters.index(i)
    newPos = (a * pos + b)%26
    encryptedMessage += formulaLetters[newPos]
  return encryptedMessage

#Decrypts messages exactly how we did in class, along with returning the decryption function
def decryptWithFormula(formula, message):
  formula = formula.replace(" ","")[formula.index("="):]
  try:
    a = int(formula[formula.index("(")+1:formula.index("x")])
  except:
    a = 1
  try:
    b = int(formula[formula.index("x")+1:formula.index(")")])
  except:
    b = 0
  m = 26-b
  n = 9
  while (a*n)%26 != 1:
    n += 2
  decryptedMessage = ""
  for i in message:
    pos = formulaLetters.index(i)
    newPos = n * (pos + m) % 26
    decryptedMessage += formulaLetters[newPos]
  return decryptedMessage, f'x = {n}(y + {m})%26'

#Random position demonstration
#Ask user to input a string
#someText = input ("Please enter a string you would like to encrypt: ")
#encryptedText = randomkeyEncrypt(someText)
#print("Your encrypted text is: " + encryptedText)

#encryptedInput = input ("Let us try to decrypt the encrypted text. Please enter the encrypted string: ")
#decryptedText = randomkeyDecrypt(encryptedInput)
#print("Your decrypted text is: " + decryptedText)

#Class decryption demonstration (Does not accept punctuation)
#formula = input("Enter an encryption function in its general form: ")
#message = input("Enter a message to be encrypted (All Caps): ")
#newMessage = encryptWithFormula(formula,message)
#print("Encrypted Message: " + newMessage)
#decrypted = decryptWithFormula(formula,newMessage)
#print("The original message is: " + decrypted[0])
#print("The decryption function is: " + decrypted[1])


# Made by John; this allows to user to choose whether they would like to encrypt or decrypt a string

# Create a loop in the case of invalid outputs
while True:

# ask user whether they want to encrypt or decrypt a string
    choice1Text = input(f"Would you like to encrypt or decrypt a string?(Please use 'E' for an encryption and 'D' for a decryption):\n")

# ask user to input a string
    if (choice1Text == "E"):
        someText = input ("Please enter a string you would like to encrypt: ")
        encrypted1Text = randomkeyEncrypt(someText)
        print("Your encrypted text is: " + encrypted1Text)

        encryptedInput = input ("Let us try to decrypt the encrypted text. Please enter the encrypted string: ")
        decrypted1Text = randomkeyDecrypt(encryptedInput)
        print("Your decrypted text is: " + decrypted1Text)
        break
    elif (choice1Text == "D"):
        otherText = input ("Please enter a string you would like to decrypt: ")
        decrypted2Text = randomkeyDecrypt(otherText)
        print("Your decrypted text is: " + decrypted2Text)

        # create another loop to see if the user would like the string to be encrypted again
        while True:
            choice2Input = input (f"Would you like this string to be encrypted again?(Please input 'Y' for yes or 'N' for no):\n")
            if (choice2Input == "Y"):
                encrypted2Text = randomkeyEncrypt(decrypted2Text)
                print("Your encrypted text is: " + encrypted2Text)
                break
            elif (choice2Input == "N"):
                break
            else:
                print("Invalid input. Please use either 'Y' or 'N'.")
        break
    else:
        print("Invalid input. Please use either 'E' or 'D' depending on what you would like to do.")