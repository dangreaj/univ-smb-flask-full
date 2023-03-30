from flask import Flask
from flask import request
import jsonify
import mysql.connector
from db import mydb

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, API!"

### Reverra les donnée JSON
@app.route("/api/log",method=['GET'])
def get_data():
    sql = "SELECT id_user,login, password FROM identity.auth"
    