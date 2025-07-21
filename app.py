# app.py
from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)
DB_NAME = 'scores.db'

# Ensure DB exists
if not os.path.exists(DB_NAME):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS scores (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            score INTEGER NOT NULL,
                            date TEXT NOT NULL
                        )''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-score', methods=['POST'])
def add_score():
    data = request.json
    name = data.get("name")
    score = data.get("score")
    date = data.get("date")
    if not all([name, score, date]):
        return jsonify({"error": "Missing fields"}), 400

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO scores (name, score, date) VALUES (?, ?, ?)", (name, score, date))
        conn.commit()

    return jsonify({"message": "Score added successfully"})

@app.route('/list-scores', methods=['GET'])
def list_scores():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("SELECT name, score, date FROM scores ORDER BY date DESC")
        results = cursor.fetchall()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
