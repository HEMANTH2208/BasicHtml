from flask import Flask, request, render_template
import sqlite3 as sql
from werkzeug.security import generate_password_hash, check_password_hash 


app = Flask(__name__)

def create_table():
    conn = sql.connect('form.db')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS formUser (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name varchar(100),
            email varchar(100),
            password varchar(100)
        )
    """)
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    Name = request.form['name']
    Email = request.form['email']
    Pass = request.form['password']

    hassed_pass = generate_password_hash(Pass)

    conn = sql.connect('form.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO formUser (name, email, password) VALUES (?, ?, ?)", (Name, Email, hassed_pass))
    conn.commit()
    conn.close()
    return "Data saved successfully"



app.run(debug = True)
