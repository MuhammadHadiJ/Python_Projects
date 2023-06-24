from info import *

Ask = input("If you want to login press 1 and if you want to sign up press 2 ")
if int(Ask) == 2:
    global un
    global pw1
    un = input("plese type a username: ")
    pw1 = input("plese type a password: ")
    pw2 = input("plese retype the password: ")
    if pw1 == pw2:
        global pw
        pw = pw1
        f = open("info.py", "w")
        f.write("User = "+'"'+un+'"'+"\n")
        f.write("Pass = "+'"'+pw+'"'+"\n")
        Ask2 = input("now would you like to login yes/no? ")
        if Ask2.upper() == "YES":
            une = input("plese enter the username ")
            pwe = input("plese enter your password ")
            if une == User and pwe == Pass:
                print("You have succesfully loged in!")
            else:
                print("Your credientials are wrong plese try again!")

    else:
        print("Your passwords did not match try again")

if int(Ask) == 1:
    une = input("plese enter the username ")
    pwe = input("plese enter your password ")
    if une == User and pwe == Pass:
        print("You have succesfully loged in!")
    else:
        print("Your credientials are wrong plese try again!")