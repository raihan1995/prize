from flask import Flask, Response
import random
import string

app = Flask(__name__)

@app.route('/digits', methods=['GET'])
def digits():
    digits = string.digits
    return ( ''.join(random.choice(digits) for i in range(7)) )
    
if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')