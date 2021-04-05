from flask import Flask, Response
import random
import string

app = Flask(__name__)

@app.route('/letters', methods=['GET'])
def letters():
    number = random.randint(5,10)
    letters = string.ascii_letters
    return ( ''.join(random.choice(letters) for i in range(number)) )

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')