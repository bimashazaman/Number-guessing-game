import random

def guess(x):
    random_number = random.randint(1, x)

    guess = 0

    while guess != random_number:
        guess = int(input("Guess a number between 1 and {}: ".format(x)))
        if guess == random_number:
            print("You guessed it!")
        elif guess < random_number:
            print("Too low!")
        else:
            print("Too high!")

guess(1000)


    # if x == random_number:
    #     return True
    # else:
    #     return False

