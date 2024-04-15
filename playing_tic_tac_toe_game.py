#!/usr/bin/python3
#Ask for position to play
#Check that position is valid
#Place X or O in that position
#Check for winner
#Switch to next player's turn
#Repeat until someone wins, or the board is full

blank_board = """
  1   2   3
1   |   |
 --- --- ---
2   |   |
 --- --- ---
3   |   |
"""

name   = input("What is your name? ")
print("Welcome to Tic Tac Toe, " + name + ". Here is our playing board:")
print(blank_board)
position = input("Enter a position (i.e., 1,1): ")
print(position)

# TODO: Check the position is valid
if len(position) != 3 or not position[0].isnumeric() or not position[2].isnumeric() or position[1] != ',':
    print("Invalid position! Please enter a position in the format 'row,column'.")

else:
  row = int(position[0])
  col = int(position[2])
if row < 1 or row > 3 or col < 1 or col > 3:
    print("Invalid position! Please enter a position within the range of 1 to 3.")

# tic-tac-toe positions
a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "

# TODO: Update the correct variable based on the position entered
if row == 1:
  if col == 1:
      a = "X"  # or "O" depending on the player
  elif col == 2:
      b = "X"  # or "O" depending on the player
  else:
      c = "X"  # or "O" depending on the player
elif row == 2:
  if col == 1:
      d = "X"  # or "O" depending on the player
  elif col == 2:
      e = "X"  # or "O" depending on the player
  else:
      f = "X"  # or "O" depending on the player
else:
  if col == 1:
      g = "X"  # or "O" depending on the player
  elif col == 2:
      h = "X"  # or "O" depending on the player
  else:
      i = "X"  # or "O" depending on the player



# print the updated board
board = f"""
  1   2   3
1 {a} | {b} | {c}
 --- --- ---
2 {d} | {e} | {f}
 --- --- ---
3 {g} | {h} | {i}
"""
print(board)
