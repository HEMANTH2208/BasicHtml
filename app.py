from flask import Flask, request, render_template
import sqlite3 as sql

app = Flask(__name__)

def create_table():
    conn = sql.connect('form.db')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS formUser (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT
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
    name = request.form['name']
    email = request.form['email']
    Pass = request.form['password']

    conn = sql.connect('form.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO formUser (name, email, password) VALUES (?, ?, ?)", (name, email, Pass))
    conn.commit()
    conn.close()
    return "Data saved successfully"

app.run(debug = True)
