#!/usr/bin/python3
#Print "What is your name? "
#Accept the user's input and store it in a variable called name
#Print "Welcome to Tic Tac Toe, [NAME THEY ENTERED]. Here is our playing board:"
#Print the board by printing the blank_board variable in your code.
#Print "Enter a position (i.e., 1,1): "
#Accept the user's input of the playing position.
#Print the position the user entered.

# this is a multiline string; it starts with three quotes
blank_board = """
  1   2   3
1   |   |
--- --- ---
2   |   |
--- --- ---
3   |   |
"""

name = input("What is your name? ")
#print("What is your name?")
print(f"Welcome to Tic Tac Toe, {name}. Here is our playing board:")
print(blank_board)
#print("Enter a position (i.e., 1,1):")
position = input("Enter a position (i.e., 1,1):")
print(f"You entered position: {position}")
