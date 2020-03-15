from flask import render_template, url_for, flash, redirect
from python_twitter import app
from python_twitter.forms import RegistrationForm, LoginForm

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
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (form.email.data == 'admin@blog.com' and form.password.data == 'password'):
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


