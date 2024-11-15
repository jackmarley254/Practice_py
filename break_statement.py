import random as r
rand_num = r.randrange(1, 20) # Generating a random number between 1 and 19
print("Number to be guesed :", rand_num)
i = 1
while True:
    print("Number Guessed :", i)
    if(i == rand_num): # if the number is correct this is the block to be executed
        print("Random Number has been guessed successfully!")
        break # Breaks and exits from the loop
    i += 1
