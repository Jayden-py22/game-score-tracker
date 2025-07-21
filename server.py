import socket
import sqlite3
import threading
import json

HOST = '127.0.0.1'
PORT = 65432
DB_NAME = 'scores.db'

def setup_database():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS scores (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            score INTEGER NOT NULL,
                            date TEXT NOT NULL
                        )''')


def handle_client(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            print("Raw data received:", data)
            if not data:
                break
            try:
                message = json.loads(data.decode())
                action = message.get("action")
                if action == "add-score":
                    name = message["name"]
                    score = message["score"]
                    date = message["date"]
                    with sqlite3.connect(DB_NAME) as db:
                        db.execute("INSERT INTO scores (name, score, date) VALUES (?, ?, ?)",
                                   (name, score, date))
                        db.commit()
                    conn.sendall(b"Score added.\n")
                elif action == "list-scores":
                    with sqlite3.connect(DB_NAME) as db:
                        cursor = db.execute("SELECT name, score, date FROM scores ORDER BY date DESC")
                        results = cursor.fetchall()
                    conn.sendall(json.dumps(results).encode())
                else:
                    conn.sendall(b"Unknown action.\n")
            except Exception as e:
                conn.sendall(f"Error: {str(e)}\n".encode())

def main():
    setup_database()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()