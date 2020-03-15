from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '3700b0f6c64981f8fa1f53d16bacb69f'

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


if __name__ == '__main__':
    app.run(debug=True)