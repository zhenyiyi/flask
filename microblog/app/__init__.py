from flask import Flask 

app = Flask(__name__)

from app import routes

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8888);




# 
# 
# kill -9 `lsof -i:5000 -t` 关闭5000端口

