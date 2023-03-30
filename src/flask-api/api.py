from flask import Flask, render_template
import json
from sqlalchemy import column
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import table
from sqlalchemy import text

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, API!"

### Reverra les donnée JSON
@app.route("/log", methods=['POST'])
def get_data():
    '''data = request.json
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
    return "Je viend de API.py"'''

    engine = create_engine("mysql://user:password@localhost/identity")

@app.route("/")
def start(): 

    with engine.connect() as connection:
        # use connection.execute(), not engine.execute()
        # select() now accepts column / table expressions positionally
        result = connection.execute(text("SELECT * FROM identity;"))

    print(result.fetchall())
    