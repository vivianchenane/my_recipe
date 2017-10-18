from app import app
from flask import redirect,request,render_template,url_for, session, flash, render_template
from .forms import LoginForm, RegisterForm

database_users = {}


recipe_list_items = []

recipe_categories = []



@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title = 'Login')

@app.route('/register', methods=['GET','POST'])
def register():
	form=RegisterForm()
	if request.method=='GET':
		return render_template('register.html', title='Register')
	
	if request.method =='POST':
		
		email = request.form.get('email')
		username = request.form.get('username')
		password = request.form.get('password')
		confirmpassword = request.form.get('cpassword')
		print('Form submitted her')
		print(confirmpassword)
	if password != confirmpassword:
			return redirect('/register')

	# database_users[username] = dict(email=email, passwword=password)
	# session['username'] = username
	return redirect('/login')


@app.route('/login', methods=['GET' ,'POST'])
def login():
	form=LoginForm()
	if request.method== 'GET':
		return render_template('index.html', form=form, title='Login')

	if request.method=='POST':
		username = request.form.get('username')
		password = request.form.get('password')
		print(username)
		# if database_users[username] and database_users[username]['password'] == password:
		# 		session['username'] = username
		return redirect ('/recipecategorylist')
		# else:
		# 		return redirect(url_for('login'))

		# 		return redirect(url_for('index'))

@app.route("/recipe_itemlist")
def recipe_itemlist():
	return render_template ('recipe_itemlist.html')

@app.route('/add_recipeitem' ,methods= ['GET', 'POST'])
def add_recipeitem():
	id = request.args.get(id)
	uname = session['username']
	if request.method == 'POST':
		name = request.form.get('name')
		description = request.form.get('description')
		category = request.form.get('category')
		user = session['username']
		id = len(recipe_list_items) + 1
		category_item = {'id': id, "name": name,"description": description, "user":user,"category":category}
		recipe_list_items.append(category_item)
		
		category_index_to_view = int(category) -1
		category_to_view = recipe_categories[category_index_to_view]
		recipeitems_to_view = []
		for item in recipe_list_items:
			if item['user'] == str(uname) and item['category']==category:
				recipeitems_to_view.append(item)
			else:
			    return render_template('recipeitem_list.html', title='Item List',category_list_itemss=recipeitems_to_view,categoryr=category_to_view)
		return render_template( 'add_recipeitem.html', title='add item', category=id)

@app.route('/add_recipecategory', methods=['GET'])
def addrecipecategory():
	return render_template ('add_recipecategory.html')

@app.route('/save_category', methods=['POST'])
def savecategory():
	user=session['username']
	print(user)
	name=request.form.get('recipename')
	description=request.form.get('description')
	print(name)
	id=len(recipe_categories) + 1
	category = {"id": id, "name":name, "description": description, "user": user}
	recipe_categories.append(category)
	return redirect('/recipecategorylist')

@app.route('/recipecategorylist')
def recipecategorylist():
	uname = session ['username']
	user_recipecategory = []
	for recipecategory in recipe_categories:
	 if recipecategory['user'] == str(uname):
		 user_recipecategory.append(recipecategory)
	else:
		return render_template('recipe_categorylist.html', title = 'Recipe Category List',recipe_categories=user_recipecategory)


