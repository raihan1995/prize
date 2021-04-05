from flask import Flask, Response
import random
import requests

app = Flask(__name__)

@app.route('/password', methods=['GET'])
def password():
    password_letters = requests.get('http://service2:5001/letters').text
    password_digits = requests.get('http://service3:5002/digits').text
    password = password_letters + password_digits
    return password
    
#@app.route('/passwordstrength/<str:password>', methods=['GET'])

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')