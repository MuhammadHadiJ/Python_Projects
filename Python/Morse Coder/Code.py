user_input = input("Enter the sentence you like to convert to morse code: ")
con = user_input.lower() 
legnth = len(con)
res = "abbb"
b = False
print(con)
i = 0
while i == 0:
    if con[i] == "a":
        res = ".- "
    if con[i] == "b":
        res = "-... "
    if con[i] == "c":
        res = "-.-. "
    if con[i] == "d":
        res = "-.. "
    if con[i] == "e":
        res = ". "
    if con[i] == "f":
        res = "..-. "
    if con[i] == "g":
        res = "--. "
    if con[i] == "h":
        res = ".... "
    if con[i] == "i":
        res = ".. "
    if con[i] == "j":
        res = ".--- "
    if con[i] == "k":
        res = "-.- "
    if con[i] == "l":
        res = ".-.. "
    if con[i] == "m":
        res = "-- "
    if con[i] == "n":
        res = "-. "
    if con[i] == "o":
        res = "--- "
    if con[i] == "p":
        res = ".--. "
    if con[i] == "q":
        res = "--.- "
    if con[i] == "r":
        res = ".-. "
    if con[i] == "s":
        res = "... "
    if con[i] == "t":
        res = "- "
    if con[i] == "u":
        res = "..- "
    if con[i] == "v":
        res = "...- "
    if con[i] == "w":
        res = ".-- "
    if con[i] == "x":
        res = "-..- "
    if con[i] == "y":
        res = "-.-- "
    if con[i] == "z":
        res = "--.. "
    if con[i] == " ":
        res = "   "
    i+=1
    while i != legnth:
        if con[i] == "a":
            res += ".- "
        if con[i] == "b":
            res += "-... "
        if con[i] == "c":
            res += "-.-. "
        if con[i] == "d":
            res += "-.. "
        if con[i] == "e":
            res += ". "
        if con[i] == "f":
            res += "..-. "
        if con[i] == "g":
            res += "--. "
        if con[i] == "h":
            res += ".... "
        if con[i] == "i":
            res += ".. "
        if con[i] == "j":
            res += ".--- "
        if con[i] == "k":
            res += "-.- "
        if con[i] == "l":
            res += ".-.. "
        if con[i] == "m":
            res += "-- "
        if con[i] == "n":
            res += "-. "
        if con[i] == "o":
            res += "--- "
        if con[i] == "p":
            res += ".--. "
        if con[i] == "q":
            res += "--.- "
        if con[i] == "r":
            res += ".-. "
        if con[i] == "s":
            res += "... "
        if con[i] == "t":
            res += "- "
        if con[i] == "u":
            res += "..- "
        if con[i] == "v":
            res += "...- "
        if con[i] == "w":
            res += ".-- "
        if con[i] == "x":
            res += "-..- "
        if con[i] == "y":
            res += "-.-- "
        if con[i] == "z":
            res += "--.. "
        if con[i] == " ":
            res += "   "
        i+=1

print("Here is the Morse version : \n" + res)