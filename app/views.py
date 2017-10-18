from app import app
from flask import redirect,request,render_template,url_for, session, flash, render_template

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title = 'Login')