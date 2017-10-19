from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	openid = StringField('openid' , validators=[DataRequired()])
	remember_me = BooleanField('remember_me',default=False)

class RegisterForm(FlaskForm):
	email = StringField('email' ,validators=[DataRequired()])
	password = PasswordField('password' ,validators=[DataRequired()])
	username = StringField('username' ,validators=[DataRequired()])
	cpassword = PasswordField('cpassword' ,validators=[DataRequired()])