from flask import Flask, Response
import random
import requests

app = Flask(__name__)

@app.route('/password', methods=['GET'])
def password():
    password_letters = requests.get('http://service2:5002/letters')
    password_digits = requests.get('http://service3:5003/digits')
    password =  letters + digits
    return password
    
#@app.route('/passwordstrength/<str:password>', methods=['GET'])

if __name__ == '__main__':
    app.run(port=5004, debug=True, host='0.0.0.0')