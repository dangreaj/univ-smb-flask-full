from flask import Flask
from flask import request
import json
import mysql.connector
from db import mydb

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, API!",met


@app.route('/api/receive_data',methods=['POST'])
def receive_data():
    data = request.json
    send_pswd_user_sql(data)
    return 'Je viens de api'

    def send_pswd_user_sql(data):
        login=[]
        login.insert(0,data[0])
        pswd = data[1]
        cursor = mydb.cursor()
        cursor.executee('SELECT * FROM auth WHERE = %s', (login))
        rows = cursor.fetchall()
        print(rows)
        result=[]
        for row in rows:
            result.append({'auth': row[0], 'password': row[1]})
            if(result[0]['password'] == pswd):
                return True
            else:
                return False