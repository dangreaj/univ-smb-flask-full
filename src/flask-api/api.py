from flask import Flask, jsonify, request
import json
import mysql.connector
#from db import mydb

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, API!"

### Reverra les donnée JSON
@app.route("/api/log", methods=['POST'])
def get_data():
    data = request.json
    login = []
    login.insert(0,data[0])
    pwd = data[1]
    cursor = mydb.cursor()
    req = "SELECT id_user,login, password FROM identity.auth  WHERE login = %s"(login)
    cursor.execute(req)
    rows = cursor.fetchall()
    res = []
    for row in rows:
        result.append({'login': row[0], 'password': row[1]})
    if (res[0]['password'] == pwd):
        return True
    else:
        return False
    return "Je viend de API.py"
    