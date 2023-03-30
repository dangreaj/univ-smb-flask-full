from flask import Flask, render_template, request
import requests

app = Flask(__name__)

## URL api.py
url = 'http://127.0.0.1:5000/api'

@app.route("/")
def start(): 
    return render_template('connect.html')


@app.route("/index", methods=['POST'])
def index():
    login = request.form['login']
    password = request.form['passwd']
    data = list([login,password])
    response = requests.post(url + "/log", json=data)
    if response.ok:         #print(response) -> <Response [200]>
        #ajouter la creation de la variable de session ici
        return render_template('start.html')
    else:
        return render_template('connect.html')



"""
@app.route("/index",methods=['GET','POST'])
def index(): 
    if(request.method == 'GET'):
        render_template('start.html')
    else:
        return render_template('connect.html')

    login = request.form['login']
    print(login)
    passwd = request.form['passwd']

    data = list([login,passwd])
    response = requests.post(url + '/log', json=data)
    print(response)
    if response.ok:
        return render_template("start.html")
    else:
        return render_template('connect.html')
"""
@app.route("/permit")
def permit():
    return render_template('UserPermit.html')

@app.route("/info")
def info():
    return render_template ('UserInfo.html')

@app.route("/inscription")
def inscription():
    return render_template ('inscription.html')