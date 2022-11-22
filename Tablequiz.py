import sqlite3
import random
import sys

con = sqlite3.connect("F1.db")
print("Let's play an F1 quiz, to exit type 'stop'")
cur = con.cursor()

def startgame():
    print("Choose which quiz? 1=drivers, 2=constructors, 3=constructors in order, 4=drivers in order, 5=runner up in order, 6=runner up")
    chosengame = input()
    if chosengame == "1":
        driversgame()
    elif chosengame =="2": 
        constructorsgame()
    elif chosengame == "3":
        consgameinorder()
    elif chosengame == "4":
        driversinorder()
    elif chosengame == "5":
        runnerinorder()
    elif chosengame == "6":
        runnersgame()
    else:
        print("Bye!")
        sys.exit()

def driversgame():
    while True:
        randyear = random.randrange(72) + 1

        cur.execute("SELECT year from years WHERE idYears = ?", (randyear,))
        year = cur.fetchone()
        cur.execute("SELECT driver_champion from years WHERE idYears = ?", (randyear,))
        id = cur.fetchone()
        cur.execute("SELECT name from drivers WHERE idDriver = ?", (id))
        right_anwser = cur.fetchone()
        print("Who won in", year[0], "?")
        N = input()
        stop_str = "stop"
        if N == stop_str:
            startgame()
        else:
            res = False
            for ele in right_anwser:
                if N == ele :
                    res = True
                break
            if res == True:
                print(str(res))
            else:
                print(str(res), ", True anwser:", right_anwser[0])


def constructorsgame():
    while True:
        randyear = random.randrange(64) + 1

        cur.execute("SELECT year from years WHERE idYears = ?", (randyear,))
        year = cur.fetchone()
        cur.execute("SELECT constructor_champion from years WHERE idYears = ?", (randyear,))
        id = cur.fetchone()
        cur.execute("SELECT name_cons FROM constructors WHERE idConstructors =?", (id))
        right_anwser = cur.fetchone()
        print("Which Constructor won in", year[0], "?")
        N = input()
        stop_str = "stop"

        if N == stop_str:
            startgame()
        else:
            res = False
            for ele in right_anwser:
                if N == ele:
                    res = True
                break
            if res == True:
                print(str(res))
            else:
                print(str(res), ", True anwser:", right_anwser[0])

def consgameinorder():
    k = 0
    p = 0
    while True:
        k = k+1
        if k == 66:
            print("You've got",p,"Points of a total 65")
            startgame()
        else:
            cur.execute("SELECT year from years WHERE idYears = ?", (k,))
            year = cur.fetchone()
            cur.execute("SELECT constructor_champion from years WHERE idYears = ?", (k,))
            id = cur.fetchone()
            cur.execute("SELECT name_cons FROM constructors WHERE idConstructors =?", (id))
            right_anwser = cur.fetchone()
            print("Which Constructor won in", year[0], "?")
            N = input()
            stop_str = "stop"
    
            if N == stop_str:
                startgame()
            else:
                res = False
                for ele in right_anwser:
                    if N == ele:
                        res = True
                    break
                if res == True:
                    print(str(res))
                    p = p+1
                else:
                    print(str(res), ", True anwser:", right_anwser[0])

def driversinorder():
    k = 0
    p = 0
    while True:
        k = k+1
        if k == 74:
            print("You've got",p,"Points from a total of 73")
            startgame()
        else:
            cur.execute("SELECT year from years WHERE idYears = ?", (k,))
            year = cur.fetchone()
            cur.execute("SELECT driver_champion from years WHERE idYears = ?", (k,))
            id = cur.fetchone()
            cur.execute("SELECT name FROM drivers WHERE idDriver =?", (id))
            right_anwser = cur.fetchone()
            print("Which Driver won in", year[0], "?")
            N = input()
            stop_str = "stop"
    
            if N == stop_str:
                startgame()
            else:
                res = False
                for ele in right_anwser:
                    if N == ele:
                        res = True
                    break
                if res == True:
                    print(str(res))
                    p = p+1
                else:
                    print(str(res), ", True anwser:", right_anwser[0])

def runnerinorder():
    k = 1
    p = 0
    while True:
        k = k+1
        if k == 74:
            print("You've got",p,"Points from a total of 72")
            startgame()
        else:
            cur.execute("SELECT year from years WHERE idYears = ?", (k,))
            year = cur.fetchone()
            cur.execute("SELECT runner_up from years WHERE idYears = ?", (k,))
            id = cur.fetchone()
            cur.execute("SELECT name FROM drivers WHERE idDriver =?", (id))
            right_anwser = cur.fetchone()
            print("Which Driver was runner up in", year[0], "?")
            N = input()
            stop_str = "stop"
    
            if N == stop_str:
                startgame()
            else:
                res = False
                for ele in right_anwser:
                    if N == ele:
                        res = True 
                    break
                if res == True:
                    print(str(res))
                    p = p+1
                else:
                    print(str(res), ", True anwser:", right_anwser[0])


def runnersgame():
    while True:
        randyear = random.randrange(72) + 2

        cur.execute("SELECT year from years WHERE idYears = ?", (randyear,))
        year = cur.fetchone()
        cur.execute("SELECT runner_up from years WHERE idYears = ?", (randyear,))
        id = cur.fetchone()
        cur.execute("SELECT name from drivers WHERE idDriver = ?", (id))
        right_anwser = cur.fetchone()
        print("Who was runner up in", year[0], "?")
        N = input()
        stop_str = "stop"
        if N == stop_str:
            startgame()
        else:
            res = False
            for ele in right_anwser:
                if N == ele :
                    res = True
                break
            if res == True:
                print(str(res))
            else:
                print(str(res), ", True anwser:", right_anwser[0])





startgame()
