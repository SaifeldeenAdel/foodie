from flask import render_template, url_for, flash, redirect, request
from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm, ChangeForm, Search
from application.models import User, Recipes
from flask_login import login_user, current_user, logout_user, login_required
from application.lookup import lookup, recipe_encode
import urllib

@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been made. You can now Log In!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", form=form)



@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('You have been logged in!', 'success')
            return redirect (next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, please check username or password', 'danger')
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('register'))


@app.route("/change", methods=["GET", "POST"])
def change():
    form = ChangeForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user and bcrypt.check_password_hash(user.password, form.old_password.data):
            if form.new_password.data == form.old_password.data:
                flash('Your new password should not be the same as your old password', 'danger')
            else:
                new_password_hash = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
                user.password = new_password_hash
                db.session.commit()
                flash('Your password has been successfully changed!', 'success')
                return redirect(url_for('home'))
        else:
            flash('Unsuccessful. Please check your username or password', 'danger')
    
    return render_template('change.html', form=form)



@app.route("/search", methods=["GET", "POST"])
@login_required
def search():
    form = Search()
    if form.validate_on_submit():
        search = lookup(form.search.data)
        return render_template("search.html", form=form, search=search)
        
        
    return render_template("search.html", form=form)



@app.route("/recipe_page" , methods=["GET", "POST"])
@login_required
def recipe_page():
    uri = request.args.get('id')
    recipe_info = recipe_encode(uri)

    user = User.query.filter_by(id=current_user.id).first()
    recipes = user.recipes
    user_recipes =[]
    for recipe in recipes:
        user_recipes.append(recipe.uri)
    
    return render_template('recipe_page.html', recipe=recipe_info, user_recipes=user_recipes)
        




@app.route("/my_recipes", methods=["GET", "POST"])
@login_required
def my_recipes():
    user = User.query.filter_by(id=current_user.id).first()
    recipes = user.recipes
    user_recipes =[]
    for recipe in recipes:
        user_recipes.append(recipe.uri)
    return render_template("my_recipes.html", recipes=recipes, user_recipes=user_recipes)



@app.route("/add_recipe", methods=["POST"])
@login_required
def add_recipe():
    uri = request.args.get('id')
    recipe_info = recipe_encode(uri)
    recipe = Recipes(uri=recipe_info['uri'], name=recipe_info['name'], ingredients=', '.join(recipe_info['ingredients']), image=recipe_info['image'], url = recipe_info['url'], user_id=current_user.id)
    db.session.add(recipe)
    db.session.commit()
    flash('Successfully added to your Recipes!', 'success')
    return redirect(url_for('my_recipes'))



@app.route("/remove_recipe", methods=["POST"])
@login_required
def remove_recipe():
    uri = request.args.get('id')
    recipe = Recipes.query.filter_by(uri=urllib.parse.unquote(uri)).first()
    db.session.delete(recipe)  
    db.session.commit()
    flash('Successfully removed from your Recipes!', 'success')
    return redirect(url_for('my_recipes'))