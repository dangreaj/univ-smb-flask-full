from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start(): 
    return render_template('connect.html')

@app.route("/index", methods=['POST'])
def index():
    login = request.form['login']
    passsword = request.form['password']
    donnees = list([login,passsword])
    response = requests.post('http://127.0.0.1:5001/api/recevoir-donnees',json=donnees)
    if response.ok:         #print(response) -> <Response [200]>
        return render_template('start.html')
    else:
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