import random
tutorial = input("Press 'i' for tutorial and press 'q' if you know how to play " )
if tutorial.upper() == "I":
    print("In this game you think of any animal and the computer will guess it after asking 10 question which you have to awnser with just a yes or no")
elif tutorial.upper() == "Q":
    print("ok then you are ready")
q1rand = 1
if q1rand == 1:
    q1 = input("is the animal you thought of small in hight ")
    if q1.upper() == "YES":
        q3 = input("is the animal an insect ")
        if q3.upper() == "Yes":
            q4 = input("does the animal fly ")
            if q4.upper() == "Yes":
                input("its a fly! ")
            elif q4.upper() == "NO":
                print("ERROR 404 Animal Not Found ")
        elif q3.upper() == "NO":
            q5 = input("Are people afraid of it ")
            if q5.upper() == "Yes":
                input("its a mouse! ")
            elif q5.upper() == "NO":
                input("its a hamster! ")
    elif q1.upper() == "NO":
        q3b = input("We ride on that animal ")
        if q3b.upper() == "YES":
            q4b = input("is it smaller than a horse ")
            if q4b.upper() == "NO":
                input("its a horse! ")
            elif q4b.upper() == "YES":
                input("its a donkey!")
        elif q3b.upper() == "NO":
            q5b = input("its a fast animal ")
            if q5b.upper() == "YES":
                q6 = input("it eats meat ")
                if q6.upper() == "YES":
                    input("its a cheatha / lion / leoperd ")
                elif q6.upper() == "NO":
                    input("its a deer / antelope ")
            elif q5b.upper() == "NO":
                q7 = input("its gigantic ")
                if q7.upper() == "YES":
                    input("its an elephant! ")
                elif q7.upper() == "NO":
                    input("its a bird! ")