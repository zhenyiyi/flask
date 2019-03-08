from flask import Flask 

app = Flask(__name__)

from app import routes


# 
# 
# kill -9 `lsof -i:5000 -t` 关闭5000端口
#
# 
# 
#  
# flask run -p 8888 -h 0.0.0.0



