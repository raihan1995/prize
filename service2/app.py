from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/letters', methods=['GET'])
def letters():

if __name__=="__main__":
    app.run(port=5001, debug=True, host='0.0.0.0')