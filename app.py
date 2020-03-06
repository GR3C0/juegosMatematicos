from os import read
from flask import Flask, escape, request, render_template, redirect
import json

from flask.helpers import url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    db = read_db()
    return render_template('index.html', db=db)

@app.route('/login', methods=['GET', 'POST'])
def login():
    db = read_db()
    return render_template('login.html', db=db)

@app.route('/bomba<id>', methods=['GET', 'POST'])
def bomba(id):
    template = "bomba{}.html".format(id)
    return render_template(template, volver=index(), enviar=comprobar_respuesta("","",""))

def comprobar_respuesta(grupo, id, respuesta):
    return

@app.route('/login_user/<grupo>/<resp>')
def check_login(grupo, resp):
    db = read_db()
    if(resp == db["resultados"]["login"]):
        print("Correcto")
        return redirect(url_for('index'))
    else:
        return redirect(render_template('login.html', db=db, msg="Resultado incorrecto bro"))

#----------------UTIL----------------------
def read_db():
    data = []
    with open('grupos.json') as db:
        data = json.load(db)
    return data

def write_db(new_data):
    data = read_db()
    with open('grupos.json', 'w', encoding='utf-8') as db:
        json.dump(data, db, ensure_ascii=False, indent=4)
    return data

def check_logged(grupo):
    db = read_db()
    return bool(db[grupo]["logged"])
#----------------UTIL----------------------