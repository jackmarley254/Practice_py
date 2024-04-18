#!/usr/bin/python3


# Print numbers 1 to 100
# For multiples of 3, print "X is a multiple of 3"
# For multiples of 5, print "X is a multiple of 5"
x = 0

for x in range(1,101):
  print(x)
  if x % 3 == 0:
    print(x, "is a multiple of 3")
  elif x % 5 == 0:
    print(x, "is a multiple of 5")
else:
	print("Have a good day")
