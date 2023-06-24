from asyncio.windows_events import NULL
import random

# system
lettercaps = ""
letterlow = ""

def lowercaps():
    letter = random.randint(1,26)
    global letterlow
    if letter == 1:
        letterlow = "a"
    if letter == 2:
        letterlow = "b"
    if letter == 3:
        letterlow = "c"
    if letter == 4:
        letterlow = "d"
    if letter == 5:
        letterlow = "e"
    if letter == 6:
        letterlow = "f"
    if letter == 7:
        letterlow = "g"
    if letter == 8:
        letterlow = "h"
    if letter == 9:
        letterlow = "i"
    if letter == 10:
        letterlow = "j"
    if letter == 11:
        letterlow = "k"
    if letter == 12:
        letterlow = "l"
    if letter == 13:
        letterlow = "m"
    if letter == 14:
        letterlow = "n"
    if letter == 15:
        letterlow = "o"
    if letter == 16:
        letterlow = "p"
    if letter == 17:
        letterlow = "q"
    if letter == 18:
        letterlow = "r"
    if letter == 19:
        letterlow = "s"
    if letter == 20:
        letterlow = "t"
    if letter == 21:
        letterlow = "u"
    if letter == 22:
        letterlow = "v"
    if letter == 23:
        letterlow = "w"
    if letter == 24:
        letterlow = "x"
    if letter == 25:
        letterlow = "y"
    if letter == 26:
        letterlow = "z"


def highercaps():
    letter2 = random.randint(1,26)
    global lettercaps
    if letter2 == 1:
        lettercaps = "A"
    if letter2 == 2:
        lettercaps = "B"
    if letter2 == 3:
        lettercaps = "C"
    if letter2 == 4:
        lettercaps = "D"
    if letter2 == 5:
        lettercaps = "E"
    if letter2 == 6:
        lettercaps = "F"
    if letter2 == 7:
        lettercaps = "G"
    if letter2 == 8:
        lettercaps = "H"
    if letter2 == 9:
        lettercaps = "I"
    if letter2 == 10:
        lettercaps = "J"
    if letter2 == 11:
        lettercaps = "K"
    if letter2 == 12:
        lettercaps = "L"
    if letter2 == 13:
        lettercaps = "M"
    if letter2 == 14:
        lettercaps = "N"
    if letter2 == 15:
        lettercaps = "O"
    if letter2 == 16:
        lettercaps = "P"
    if letter2 == 17:
        lettercaps = "Q"
    if letter2 == 18:
        lettercaps = "R"
    if letter2 == 19:
        lettercaps = "S"
    if letter2 == 20:
        lettercaps = "T"
    if letter2 == 21:
        lettercaps = "U"
    if letter2 == 22:
        lettercaps = "V"
    if letter2 == 23:
        lettercaps = "W"
    if letter2 == 24:
        lettercaps = "X"
    if letter2 == 25:
        lettercaps = "Y"
    if letter2 == 26:
        lettercaps = "Z"

highercaps()
first = lettercaps
lowercaps()
second = letterlow
lowercaps()
third = letterlow
lowercaps()
fourth = letterlow
highercaps()
fifth = lettercaps
highercaps()
sixth = lettercaps
lowercaps()
seventh = letterlow
lowercaps()
eighth = letterlow
lowercaps()
nineth = letterlow
lowercaps()
tenth = letterlow
highercaps()
eleventh = lettercaps
lowercaps()
twelth = letterlow
highercaps()
thirteenth = lettercaps

print('Your uniqe password is "' + first+second+third+fourth+fifth+sixth+seventh+eighth+nineth+tenth+eleventh+twelth+thirteenth+'"')
