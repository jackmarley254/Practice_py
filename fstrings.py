#!/usr/bin/python3
#Get two numbers as input from the user
#Convert the inputs to floats
#Divide one number by the other
#Print the result, rounded to 3 digits using f-strings

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_1 = float(num_1)
num_2 = float(num_2)

results = num_1 / num_2
print(f"The answer to {num_1} divided by {num_2} is {results:.3f}")
