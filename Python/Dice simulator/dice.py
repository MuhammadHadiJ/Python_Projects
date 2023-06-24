import random

roll_dice = input("Would you like to roll the dice? ")
need_to_roll = False
if roll_dice.upper() == "YES":
    print(str(random.randint(0, 6)) + " is your number")
    close = input("Would you like to close the program (yes/no) ")
    if close.upper() == "NO":
        roll_dice = input("Would you like to roll the dice again (yes/no)? ")
        if roll_dice.upper() == "YES":
            print(str(random.randint(0, 6)) + " is your number")
            close = input("To close the program press 'ENTER' ")

