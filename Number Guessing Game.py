import random 

# create random number
r = random.randint(1, 10) 
# create the input number
guess = int(input("Enter an integer 1, 10 "))

# start testing by compare the random number (r) with the input number (guess)
if True: 
    if guess < r:
        print ("your number is lower. Try again ")
        guess = int(input("Enter and integer 1, 10 "))
    
    elif guess > r:
        print ("your number is higher. Try again ")
    guess = int(input("Enter an integer from 1, 10 "))
    print ("YOU GUESSED IT!")
