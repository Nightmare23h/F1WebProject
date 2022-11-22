from flask import Flask,render_template,request
import sqlite3
import random
import sys


app = Flask(__name__)


def year():
    con = sqlite3.connect("F1.db")  
    cur = con.cursor()
    randyear = random.randrange(72) + 1
    cur.execute("SELECT year from years WHERE idYears = ?", (randyear,))
    year = cur.fetchone()
    yeartbd = str(year[0])
    cur.close()
    return yeartbd, randyear

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


# This was my Way: 
# @app.route('/form', methods = ['POST', 'GET'])
# def data():
#     if request.method == 'GET':
#         func = year()
#         ans = str(func[0])
#         driver = whodriver(str(func[1]))
#         return render_template("form.html", year=ans, test=driver )
#     if request.method == 'POST':
#         form_data = request.form
#         driver2 = form_data["test"]
#         if driver2 == form_data["answer"]:
#             print("Gut")
#         else: 
#             print("Nix gut")
#         func = year()
#         ans = str(func[0])
#         driver = whodriver(str(func[1]))
#         return render_template("form.html", year=ans, test=driver )
#  

# This is better (But not my way): 
@app.route('/form', methods = ['POST', 'GET'])
def data():
    y, y_id = year() # for next game
    if request.method == 'POST':
        form_data = request.form
        winner = whodriver(form_data["year_id"])
        answer = form_data["answer"]
        if winner == answer:
            return render_template("form.html", year=y, year_id=y_id, result="Correct!")
        else: 
            return render_template("form.html", year=y, year_id=y_id, result=f'Wrong! In the year {form_data["year"]} {winner} won!')
    return render_template("form.html", year=y, year_id=y_id)
