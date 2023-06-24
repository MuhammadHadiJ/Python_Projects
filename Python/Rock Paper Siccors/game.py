import random
import time
def game():
    rock = 'Rock'
    paper = 'Paper'
    scissors = 'Scissors'
    my_score = 0
    his_score = 0
    while my_score < 5 and his_score < 5:
        enmy_chose = random.choice([rock, paper, scissors])
        chose = input("chose between (R)ock (P)aper and (S)cissors ")
        if chose.upper() == 'R':
            chose = 'Rock'
        elif chose.upper() == 'P':
            chose = 'Paper'
        else:
            chose = 'Scissors'
        print(enmy_chose + ' Vs ' + chose)
        if enmy_chose.upper() == 'ROCK' and chose.upper() == 'ROCK':
            my_score += 1
            his_score += 1
            print("enemy score: " + str(his_score))
            print("your score: " + str(my_score))
            time.sleep(3)
        elif enmy_chose.upper() == 'PAPER' and chose.upper() == 'ROCK':
            my_score += 0
            his_score += 1
            print("enemy score: " + str(his_score))
            print("your score: " + str(my_score))
            time.sleep(3)
        elif enmy_chose.upper() == 'SCISSORS' and chose.upper() == 'ROCK':
            my_score += 1
            his_score += 0
            print("enemy score: " + str(his_score))
            print("your score: " + str(my_score))
            time.sleep(3)
        elif enmy_chose.upper() == 'ROCK' and chose.upper() == 'PAPER':
            my_score += 1
            his_score += 0
            print("enemy score: " + str(his_score))
            print("your score: " + str(my_score))
            time.sleep(3)
        elif enmy_chose.upper() == 'PAPER' and chose.upper() == 'PAPER':
            my_score += 1
            his_score += 1
            print("enemy score: " + str(his_score))
            print("your score: " + str(my_score))
            time.sleep(3)
        elif enmy_chose.upper() == 'SCISSORS' and chose.upper() == 'PAPER':
            my_score += 0
            his_score += 1
            print("enemy score: " + str(his_score))
            print("your score: " + str(my_score))
            time.sleep(3)
        elif enmy_chose.upper() == 'ROCK' and chose.upper() == 'SCISSORS':
            my_score += 0
            his_score += 1
            print("enemy score: " + str(his_score))
            print("your score: " + str(my_score))
            time.sleep(3)
        elif enmy_chose.upper() == 'PAPER' and chose.upper() == 'SCISSORS':
            my_score += 1
            his_score += 0
            print("enemy score: " + str(his_score))
            print("your score: " + str(my_score))
            time.sleep(3)
        elif enmy_chose.upper() == 'SCISSORS' and chose.upper() == 'SCISSORS':
            my_score += 1
            his_score += 1
            print("enemy score: " + str(his_score))
            print("your score: " + str(my_score))
            time.sleep(3)
    
game()
