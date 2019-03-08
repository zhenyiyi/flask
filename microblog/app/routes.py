from app import app

@app.route('/')

@app.route('/index')

def index():
	return "Hello, World!"
# 	user = {'username' : 'xiaoying'}

# 	return '''
# <!DOCTYPE html>
# <html>
# <head>
# 	<title>Home Page - fenglin</title>
# </head>
# <body>
# 	<h1>Hello, ''' + user['username'] + ''' !</h1>
# </body>
# </html> '''



	