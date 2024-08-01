#This program is the starter code for the Programming Caesar's Cipher Project. 
# This code is inspired by Cracking Codes with Python: An Introduction to Building and Breaking Ciphers by Al Sweigart https://www.nostarch.com/crackingcodes (BSD Licensed)

# Global variables
possibleCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
initialPosition = 0
ShiftedPosition = 0
ShiftedMessage = ""

# Run code

# Introduction
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only choose from the following characters: " + possibleCharacters + "\n\nLet's get started!\n")

# Receive user input
initialMessage = input("What is your message? ")
key = int(input("What is the key value?(Pick a number from 0 to 25)"))
mode = input("Do you want to encrypt or decrypt? ")
# Encrypt or decrypt the message

for character in initialMessage:
  if character in possibleCharacters:
    initialPosition = possibleCharacters.find(character)
    if mode.lower() == "encrypt":
      ShiftedPosition = initialPosition + key
    elif mode.lower() == "decrypt":
      ShiftedPosition = initialPosition - key
    if ShiftedPosition >= len(possibleCharacters):
      ShiftedPosition = ShiftedPosition - len(possibleCharacters)
    elif ShiftedPosition < 0:
      ShiftedPosition = ShiftedPosition + len(possibleCharacters)

    ShiftedMessage = ShiftedMessage + possibleCharacters[ShiftedPosition]
  else:
    ShiftedMessage = ShiftedMessage + character
# Print the shifted message
print("Your " + mode.lower()+"ed message is: " + ShiftedMessage)