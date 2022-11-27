import sqlite3
import random 




def yearfordriver():
    con = sqlite3.connect("F1.db")  
    cur = con.cursor()
    randyeard = random.randrange(72) + 1
    cur.execute("SELECT year from years WHERE idYears = ?", (randyeard,))
    year = cur.fetchone()
    yeartbddriver = str(year[0])
    cur.close()
    return yeartbddriver, randyeard

def whodriver(x):    
    con = sqlite3.connect("F1.db")
    cur = con.cursor()
    cur.execute("SELECT driver_champion from years WHERE idYears = ?", (x,))
    id = cur.fetchone()
    cur.execute("SELECT name from drivers WHERE idDriver = ?", (id))
    right_anwser = cur.fetchone()
    driver = str(right_anwser[0])
    cur.close()
    return driver

def driverio(k):
    con = sqlite3.connect("F1.db")
    cur = con.cursor()
    cur.execute("SELECT year from years WHERE idYears = ?", (k,))
    yearx = cur.fetchone()
    cur.execute("SELECT driver_champion from years WHERE idYears = ?", (k,))
    id = cur.fetchone()
    cur.execute("SELECT name FROM drivers WHERE idDriver =?", (id))
    right_anwser = cur.fetchone()
    driver = str(right_anwser[0])
    year = str(yearx[0])
    return driver, year
    


def yearforconstructor():
    con = sqlite3.connect("F1.db")
    cur = con.cursor()
    randyearc = random.randrange(64) + 1
    cur.execute("SELECT year from years WHERE idYears = ?", (randyearc,))
    year = cur.fetchone()
    yeartbdcons = str(year[0])
    cur.close()
    return yeartbdcons, randyearc


def whoconstructor(x):
    con = sqlite3.connect("F1.db")
    cur = con.cursor()
    cur.execute("SELECT constructor_champion from years WHERE idYears = ?", (x,))
    id = cur.fetchone()
    cur.execute("SELECT name_cons FROM constructors WHERE idConstructors =?", (id))
    right_anwser = cur.fetchone()
    constructor = str(right_anwser[0])
    cur.close()
    return constructor

