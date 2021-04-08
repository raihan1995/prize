from flask import Flask, Response, request
import random
import requests

app = Flask(__name__)

@app.route('/password', methods=['GET'])
def password():
    password_letters = requests.get('http://service2:5001/letters').text
    password_digits = requests.get('http://service3:5002/digits').text
    password = password_letters + password_digits
    return password
    
@app.route('/getPassStrength', methods=["POST"])
def getPassStrength():
    data_sent = request.data.decode('utf-8')
    password = data_sent
    mypassword = len(password)
    if mypassword >= 13:
        return "strong password"
    else:
        return "weak password"


if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')