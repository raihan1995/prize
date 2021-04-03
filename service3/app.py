from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/digits', methods=['GET'])
def digits():

if __name__=="__main__":
    app.run(port=5002, debug=True, host='0.0.0.0')