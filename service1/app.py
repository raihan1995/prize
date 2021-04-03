from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask import render_template, redirect, url_for, request
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@34.89.53.51/prize_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

db.create_all()

class prize(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prize = db.Column(db.String(50), nullable=False)

#buttons = ["Generate Password"]

@app.route("/", methods=['GET'])
@app.route("/home")
def home():
#     letters = requests.get("http://service2:5001/"")
#     digits = requests.get("http://service3:5002/"")
    return render_template("home.html", title='Home')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')