#!/usr/bin/python3
# Greet the user
name = str(input("Hello! What's your name? "))
print("Hello", name + "!", "Let's see if it's time to leave this party.")

# Ask is the party is awkward
is_awkward = str(input("Is it awkward? "))
# If the user responds 'yes', print "Leave!"
# Otherwise, print the string "Stay and par-tay"

if is_awkward == 'yes':
  print('Leave!')
if is_awkward == 'no':
  print('Stay and par-tay')  
else:
  print('Go back to the kitchen')
