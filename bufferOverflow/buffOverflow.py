from flask import Flask, render_template, redirect, url_for, request, session, abort
import string
import random
import subprocess

app = Flask(__name__)
chars=string.ascii_letters + string.digits
app.secret_key = ''.join(random.choice(chars) for i in range(25))

    

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        textInserted=request.form['textsend']
        result = subprocess.run(['./exploitable', textInserted], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        session['code']=result.returncode
        if result.returncode<0:
            session['output']="Segmentation Fault (core dumped)"
        else:
            session['output']=result.stdout.decode('utf-8')
        return redirect(url_for('output'))
    return render_template('home.html', error=error)

@app.route('/output', methods=['GET'])
def output():
    if 'output' in session and session['output'] != '':
        return render_template('output.html')
    else:
        abort(403)
        
if __name__ == '__main__':
    app.run(debug=True, port=5001) # run the flask app on debug mode


#<h3> Welcome, {{session['user_name']}}! </h3>