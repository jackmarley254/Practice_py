#!/usr/bin/python3

# Original instructions: Print the sum of the odd numbers between 10 and 25
# Add print statements to debug the code
total = 0
print("Before the loop total is", total)
for i in range(10, 26):
  if i % 2 == 1:
    print(i)
    total += i
print("After the loop total is", total)


# What is wrong with the code? (answer in a comment)
# Total is missing the equals sign so that i increaments the total
# The range is missing the first number so that it starts at 10
#
