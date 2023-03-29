from flask import Flask
from flask import request
import json
import mysql.connector
from db import mydb

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, API!"

