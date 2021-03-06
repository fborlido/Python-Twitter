from flask import render_template, url_for, flash, redirect
from python_twitter import app, db, bcrypt
from python_twitter.forms import RegistrationForm, LoginForm
from python_twitter.models import User, Post
from flask_login import login_user, current_user, logout_user

posts = [
    {
        'author': 'good good sir',
        'content': 'actually very good',
        'date_posted': 'years and years ago'
    },
    {
        'author': 'good good sir!',
        'content': 'actually very good!',
        'date_posted': 'years and years ago!'
    },
    {
        'author': 'good good sir!!',
        'content': 'actually very good!!',
        'date_posted': 'years and years ago!!'
    },
    {
        'author': 'good good sir!!',
        'content': 'actually very good!!',
        'date_posted': 'years and years ago!!'
    },
    {
        'author': 'good good sir!!',
        'content': 'actually very good!!',
        'date_posted': 'years and years ago!!'
    },
    {
        'author': 'good good sir!!',
        'content': 'actually very good!!',
        'date_posted': 'years and years ago!!'
    },
    {
        'author': 'good good sir!!',
        'content': 'actually very good!!',
        'date_posted': 'years and years ago!!'
    },
    {
        'author': 'good good sir!!',
        'content': 'actually very good!!',
        'date_posted': 'years and years ago!!'
    }
]

@app.route("/")
@app.route("/home")
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/profile")
def profile():
    return render_template('profile.html', title='Profile')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. Please Log In', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))