import sqlite3
from flask import Flask, render_template, redirect, url_for, request, session, abort
import string
import random
import subprocess

app = Flask(__name__)
chars=string.ascii_letters + string.digits
app.secret_key = ''.join(random.choice(chars) for i in range(25))

    

@app.route('/sql', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        insertedUser=request.form['username']
        insertedPassword=request.form['password']
        con = sqlite3.connect('example.db')
        cur = con.cursor()
        print(insertedUser)
        print(insertedPassword)
        cur.execute("SELECT name, surname FROM users WHERE username = '%s' and password = '%s'"% (insertedUser, insertedPassword))
        rows = cur.fetchall()
        returnObject={}
        returnObject['fetched']=rows
        return returnObject
    return render_template('sqlLogin.html', error=error)

@app.route('/buffer', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        textInserted=request.form['textsend']
        result = subprocess.run(['./exploitable', textInserted], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        returnedObject = {}
        returnedObject['code'] = -1*result.returncode
        if result.returncode<0:
            returnedObject['output']="Segmentation Fault (core dumped)"
        else:
            returnedObject['output']=result.stdout.decode('utf-8')
        return returnedObject
    return render_template('buffer.html', error=error)

        
if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.2', port=5000) # run the flask app on debug mode


#<h3> Welcome, {{session['user_name']}}! </h3>