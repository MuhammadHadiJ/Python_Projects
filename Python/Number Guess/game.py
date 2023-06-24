import time
import random
import os
from turtle import color
till_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
till_twenty = [11,12,13,14,15,16,17,18,19,20]
os.system('color 4f')

awnser = random.randint(0, 20)
print("The Game has selected a value between 0-20 your objective is to find the valu through givin hints ")
if awnser % 5 == 0:
    print("The number is divisible by five")
elif awnser % 5 != 0:
    print("The number is not divisible by five")
guess1 = input("Now with the givin hint try your first guess: ")
if guess1 == str(awnser):
    print("you guessed it correct on the first try!")
    time.sleep(2)
else:
    print("the awnser is wrong but dont worry here is the second hint:")
    if awnser % 2 == 0:
        print("The awnser is an even number")
    elif awnser % 2 != 0:
        print("the number is an odd one")
    guess2 = input("Now with the givin hint try your second guess: ")
    if guess2 == str(awnser):
        print("you guessed it correct on the second try")
        time.sleep(2)
    else:
        print("the awnser is wrong but dont worry here is the third hint:")
        if awnser in till_ten:
            print("The last hint is that the number is between 1-10")
        elif awnser in till_twenty:
            print("The last hint is that the number is between 11-20")
        guess3 = input("Now with the givin hint try your third guess: ")
        if guess3 == str(awnser):
            print("well atleast you finally guessed it")
            time.sleep(2)
        else:
            print("you lost the awnser is " + str(awnser))
            time.sleep(2)

