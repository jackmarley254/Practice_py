#!/usr/bin/python3

age = input("Enter your age ")
age = int(age)
if age == 5:
    print('Proceed to kindergarten')
elif age == 6 and age <= 17:
    print('Attend upper primary')
elif age >= 17:
    print("Go to college\n")
