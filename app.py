# Store this code in 'app.py' file

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os


secret_key = str(os.urandom(24))


app = Flask(__name__)


app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'rakshu'
app.config['MYSQL_PASSWORD'] = 'Rakshu@123'
app.config['MYSQL_DB'] = 'login'

mysql = MySQL(app)

	
@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['username'] = account['username']
			a=username
			print(a)
			msg = 'Logged in successfully !'
			a=username
			return render_template('index3.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)
@app.route("/start", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            # pass
            d_dtcn()
            return render_template("index.html")
    else:
        # pass # unknown
        return render_template("index.html")
def get_data_from_html():
        pay = request.form['username']
        print ("Pay is " + pay)
        return "Data sent. Please check your program log"

@app.route('/')
def index1():
    return render_template('index.html')

@app.route('/index2', methods= ['POST','GET'])
def index2():
        #index2 = request.form
        #return render_template('index2.html')
	os.system("dir")
	os.system('python3 driverdrowsy1.py -p shape_predictor_68_face_landmarks.dat -a alarm.wav')
	return render_template('index3.html')
@app.route('/index4', methods= ['POST','GET'])
def index4():
        #index2 = request.form
        #return render_template('index2.html')
	os.system("dir")
	os.system('python3 driverdrowsy.py -p shape_predictor_68_face_landmarks.dat -a alarm.wav')
	return render_template('index3.html')
   
if __name__ == "__main__":
    app.run(host='0.0.0.0')
@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password or not email:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO accounts VALUES (% s, % s, % s)', (username, password, email, ))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)
