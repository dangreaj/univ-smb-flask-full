from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start(): 
    return render_template('start.html')

@app.route("/connect")
def connect():
    return render_template('connect.html')

@app.route("/permit")
def permit():
    return render_template('UserPermit.html')

@app.route("/info")
def info():
    return render_template ('UserInfo.html')


    