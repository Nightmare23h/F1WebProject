from flask import Flask,render_template,request, session
from functions import yearfordriver, whodriver, yearforconstructor, whoconstructor, driverio, constructorio
import os
#Moin
app = Flask(__name__)

app.config['SECRET_KEY']='moinmeister'


@app.route('/__github_webhook', methods=['POST'])
def github_webhook():
    os.system("git pull")
    os.system("touch /var/www/nightmare23h_pythonanywhere_com_wsgi.py")
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
@app.route('/iodriver', methods = ['POST', 'GET'])
def driverioquiz():
    if request.method == 'GET':
        session["defYear"]=1
        session["points"]=0
    elif request.method == 'POST':
        if (session["defYear"]) % 73 + 1 == 2:
            session["points"]=0
        y_idold = session["defYear"]
        driverold, yearold = driverio(y_idold)
        session["defYear"] = (session["defYear"]) % 73 + 1
        y_id = session["defYear"]
        _ , year = driverio(y_id)
        form_data = request.form
        answer = form_data["answer"]
        if driverold == answer:
            session["points"] = session["points"] + 1
            print(session["points"], "of 73")
            return render_template("iodriver.html", year=year, year_id=y_id, points=session["points"], result="Correct!")
        else:
            return render_template("iodriver.html", year=year, year_id=y_id, points=session["points"], result=f'Wrong! In the year {yearold} {driverold} won!')
    return render_template("iodriver.html", year="2022", year_id=1)

@app.route('/iocons', methods = ['POST', 'GET'])
def driverioquiz():
    if request.method == 'GET':
        session["defYear"]=1
        session["points"]=0
    elif request.method == 'POST':
        if (session["defYear"]) % 64 + 1 == 2:
            session["points"]=0
        y_idold = session["defYear"]
        driverold, yearold = constructorio(y_idold)
        session["defYear"] = (session["defYear"]) % 64 + 1
        y_id = session["defYear"]
        _ , year = constructorio(y_id)
        form_data = request.form
        answer = form_data["answer"]
        if driverold == answer:
            session["points"] = session["points"] + 1
            print(session["points"], "of 64")
            return render_template("iocons.html", year=year, year_id=y_id, points=session["points"], result="Correct!")
        else:
            return render_template("iocons.html", year=year, year_id=y_id, points=session["points"], result=f'Wrong! In the year {yearold} {driverold} won!')
    return render_template("iocons.html", year="2022", year_id=1)