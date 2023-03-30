from flask import Flask, render_template

app = Flask(__name__)

## URL api.py
url = 'http://127.0.0.1:5001/api'

@app.route("/")
def start(): 
    login = request.form['login']
    passwd = request.form['passwd']
    data = list([login,passswd])
    response = request.post(url + '/log', json=data)

    return render_template('connect.html')

@app.route("/index", methods=['POST'])
def index():
        return render_template('start.html')

@app.route("/permit")
def permit():
    return render_template('UserPermit.html')

@app.route("/info")
def info():
    return render_template ('UserInfo.html')

@app.route("/inscription")
def inscription():
    return render_template ('inscription.html')