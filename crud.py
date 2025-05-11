import sqlite3

DB_NAME = "scores.db"

def add_player(name):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO players (name) VALUES (?)", (name,))
        conn.commit()

def add_score(player_id, score, date):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "INSERT INTO scores (player_id, score, date) VALUES (?, ?, ?)",
            (player_id, score, date)
        )
        conn.commit()

def get_all_scores():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("""
            SELECT scores.id, players.name, scores.score, scores.date
            FROM scores
            JOIN players ON scores.player_id = players.id
            ORDER BY scores.date DESC
        """)
        return cursor.fetchall()

def update_score(score_id, new_score):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("UPDATE scores SET score = ? WHERE id = ?", (new_score, score_id))
        conn.commit()

def delete_score(score_id):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("DELETE FROM scores WHERE id = ?", (score_id,))
        conn.commit()

# Retrieve scores that fall within a specific date range
def get_scores_in_date_range(start_date, end_date):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("""
            SELECT scores.id, players.name, scores.score, scores.date
            FROM scores
            JOIN players ON scores.player_id = players.id
            WHERE scores.date BETWEEN ? AND ?
            ORDER BY scores.date DESC
        """, (start_date, end_date))
        return cursor.fetchall()