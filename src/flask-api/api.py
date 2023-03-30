from flask import Flask, render_template
import json
from sqlalchemy import column
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import table
from sqlalchemy import text
import sqlalchemy as db

app = Flask(__name__)
engine = create_engine("mysql://new_user:password@localhost/identity")

@app.route("/")
def hello():
    return "Hello, API!"

### Reverra les donnée JSON
@app.route("/log", methods=['POST'])
def get_data():
    data = request.json
    login = []
    login.insert(0,data[0])
    pwd = data[1]
    cursor = db.cursor()
    with engine.connect() as connection:
        result = connection.execute(text("SELECT id_user,login, password FROM identity.auth  WHERE login = %s"(login)))
        rows = result.fetchall()
        res = []
        for row in rows:
            result.append({'login': row[0], 'password': row[1]})
        if (res[0]['password'] == pwd):
            return True
        else:
            return False
        return "Je viend de API.py"