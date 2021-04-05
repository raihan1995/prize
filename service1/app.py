from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask import render_template, redirect, url_for, request
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@34.89.53.51/prize_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

db.create_all()

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(50), nullable=False)

# class PasswordStrength(FlaskForm):
#     password = StringField('Password', validators=[DataRequired()])
#     submit = SubmitField('Check Password Strength')

#buttons = ["Generate Password"]

@app.route("/", methods=['GET'])
@app.route("/home")
def home():
    #password = requests.get('http://service4:5004/password')
    return render_template("home.html", title='Home')

if __name__ == '__main__':
    app.run(port=5000,debug=True, host='0.0.0.0')