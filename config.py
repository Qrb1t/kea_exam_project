import os

from flask import Flask
from flaskext.mysql import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__, instance_relative_config=True)
CORS(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'Qrb1t'
app.config['MYSQL_DATABASE_PASSWORD'] = 'HPzPA3rNEvsht3Dz'
app.config['MYSQL_DATABASE_DB'] = 'w3school_tutorial'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass