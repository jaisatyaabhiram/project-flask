from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)

class Item(db.model):
    name = db.Column(db.String(length=30))

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/market')
def market_page():
    items = [
        {"id":1,"name":"bottle","price":200},
        {"id":2,"name":"Pen","price":10},
        {"id":3,"name":"box","price":20},
        {"id":4,"name":"phone","price":2000}
    ]
    return render_template('market.html',items=items)

