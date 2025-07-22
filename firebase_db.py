import firebase_db
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add-score', methods=['POST'])
def add_score():
    data = request.json
    name = data.get("name")
    score = data.get("score")
    date = data.get("date")
    if not all([name, score, date]):
        return jsonify({"error": "Missing fields"}), 400

    firebase_db.add_score(name, score, date)
    return jsonify({"message": "Score added successfully"})

@app.route('/list-scores', methods=['GET'])
def list_scores():
    scores = firebase_db.get_scores()
    return jsonify(scores)