from flask import Flask,render_template,request
from functions import yearfordriver, whodriver, yearforconstructor, whoconstructor
import os
 
app = Flask(__name__)

@app.route('/__github_webhook', methods=['POST'])
def github_webhook():
    os.system("git pull")
    return "done", 200


@app.route('/')
def mainpage():
    return render_template("mainpage.html")
     

# This is better (But not my way): 
#Drivers Quiz Random
@app.route('/rnddriver', methods = ['POST', 'GET'])
def rnddriverquiz():
    y, y_id = yearfordriver() # for next game
    if request.method == 'POST':
        form_data = request.form
        winner = whodriver(form_data["year_id"])
        answer = form_data["answer"]
        if winner == answer:
            return render_template("rnddriver.html", year=y, year_id=y_id, result="Correct!")
        else: 
            return render_template("rnddriver.html", year=y, year_id=y_id, result=f'Wrong! In the year {form_data["year"]} {winner} won!')
    return render_template("rnddriver.html", year=y, year_id=y_id)
#Constructors Quiz Random
@app.route('/rndcons', methods = ['POST', 'GET'])
def rndconquiz():
    y, y_id = yearforconstructor()
    if request.method == 'POST':
        form_data = request.form
        winner = whoconstructor(form_data["year_id"])
        answer = form_data["answer"]
        if winner == answer:
            return render_template("rndcon.html", year=y, year_id=y_id, result="Correct!")
        else: 
            return render_template("rndcon.html", year=y, year_id=y_id, result=f'Wrong! In the year {form_data["year"]} {winner} won!')
    return render_template("rndcon.html", year=y, year_id=y_id)
#Drivers Quiz IO

