from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
	user = {'username' : 'yangyang'}
	posts = [
		{
			'author' : {'username' : 'xiaoying'},
			'body' : 'Beautiful day in Portland!'
		},
		{
			'author' : {'username' : 'mama'},
			'body' : 'The Avengers movie was so cool!'
		}
	]
	return render_template('index.html', title='Home Page',user=user, posts=posts)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In',form=form)


	