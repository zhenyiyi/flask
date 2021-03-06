from flask import Flask 
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import  Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app=app)

login.login_view = 'login'

from app import routes, models


# 
# 
# kill -9 `lsof -i:5000 -t` 关闭5000端口
#
# 
# 
# http://www.cnblogs.com/adobe-lin/p/9843562.html
# flask run -p 8888 -h 0.0.0.0
#
# cryptographic key 秘钥


