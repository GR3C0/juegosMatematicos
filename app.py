from flask import Flask, escape, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', db=read_db())

@app.route('/login')
def login():
    return render_template('login.html', db=read_db())

@app.route('/bomba<id>')
def bomba(id):
    template = "bomba{}.html".format(id)
    return render_template(template)

def read_db():
    data = []
    with open('grupos.json') as db:
        data = json.load(db)
        
    return data