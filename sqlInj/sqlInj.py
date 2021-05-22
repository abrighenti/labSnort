import sqlite3
from flask import Flask, render_template, redirect, url_for, request, session, abort
import string
import random

'''
#cur.execute(CREATE TABLE users
#               (name, surname, username, password))

# Insert a row of data
for i in range(5):
    cur.execute("INSERT INTO users VALUES ('v{}', 'v{}', 'victim{}', 'victim{}')".format(i,i,i,i))

con.commit()

con.close()

# Never do this -- insecure!
#symbol = 'RHAT'
#cur.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
'''

app = Flask(__name__)
chars=string.ascii_letters + string.digits
app.secret_key = ''.join(random.choice(chars) for i in range(25))

    

@app.route('/', methods=['GET', 'POST'])
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
    return render_template('login.html', error=error)

        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) # run the flask app on debug mode


#<h3> Welcome, {{session['user_name']}}! </h3>