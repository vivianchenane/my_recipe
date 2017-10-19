from app import app
from flask import redirect,request,render_template,url_for, session, flash
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
		
	
	if password != confirmpassword:
		flash(u'password dont match')
		return redirect('/register')


	database_users[username] = dict(email=email, passwword=password)
	session['username'] = username
	return redirect('/recipecategorylist')


@app.route('/login', methods=['GET' ,'POST'])
def login():
    form=LoginForm()
    if request.method== 'GET': 
        return render_template('index.html', form=form, title='Login') 

    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            if database_users[username] and database_users[username]['password'] == password:
                session['username'] = username
               
			   
                return redirect(url_for('recipecategorylist'))
            else:
                return redirect(url_for('login'))
        
        except (KeyError, ValueError):
            flash('login failed')
            return redirect(url_for('index'))


@app.route("/recipe_itemlist")
def recipe_itemlist():
	return render_template ('recipe_itemlist.html')

@app.route('/add_recipeitem' ,methods= ['GET', 'POST'])
def add_recipeitem():
	id = request.args.get('id')
	usern = session['username']
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
			if item['user'] == str(usern) and item['category']==category:
				recipeitems_to_view.append(item)
		return render_template('recipe_itemlist.html', title='Item List',category_list_itemss=recipeitems_to_view,category=category_to_view)
		
	return render_template( 'add_recipeitem.html', title='add item', category=id)

@app.route('/add_recipecategory')
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
	for category in recipe_categories:
	 if category['user'] == str(uname):
		 user_recipecategory.append(category)
	else:
		return render_template('recipe_categorylist.html', title = 'Recipe Category List',category_items=user_recipecategory)



@app.route('/viewitems')
def view_recipeitems():
	id=request.args.get('id')
	uname = session['username']
	if id == None:
		return redirect('/recipecategorylist')

	category_index_to_view = int(id) -1
	category_to_view = recipe_categories[category_index_to_view]
	recipeitems_to_view = []
	for item in recipe_list_items:
		if item['user'] ==str(uname) and item['category'] ==id:
			recipeitems_to_view.append(item)
	
	return render_template('recipe_itemlist.html', title=' Recipe Item List',category_list_itemss=recipeitems_to_view, category=category_to_view)

@app.route('/editcategory')
def edit_category():
	id=request.args.get('id')
	if id ==None:
		return redirect('/recipecategorylist')
	index_to_edit = int(id) - 1
	category_to_edit=recipe_categories[index_to_edit]
	return render_template('edit_category.html',category=category_to_edit)


@app.route('/update_category', methods=['POST'])
def update_category():
	uname = session['username']
	if request.method =='POST':
		id = request.form.get('id')
		name = request.form.get('name')
		description = request.form.get('description')
		user = session['username']

		for item_to_update in recipe_categories:
			if item_to_update['id'] == int(id):
				item_to_update['name'] = name
				item_to_update['description'] = description
				break
		categories_to_view = []
		for item in recipe_categories:
			if item['user']==str(uname):
				categories_to_view.append(item)
		
		return render_template('recipe_categorylist.html', title='Recipe List',category_items=categories_to_view)      

@app.route('/delete_category')
def deletec():
	id=request.args.get('id')
	if id==None:
		 return redirect('/recipecategorylist')
	index_to_delete = int(id)-1
	del recipe_categories[index_to_delete]
	return redirect('/recipecategorylist')
	
@app.route('/delete_category_test')
def deletecTest():
	id=request.args.get('id')
	if id==None:
		 return redirect('/recipecategorylist')
	index_to_delete = int(id)-1
	del recipe_categories[index_to_delete]
	return redirect('/recipecategorylist')

	





