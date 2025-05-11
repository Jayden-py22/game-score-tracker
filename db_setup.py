import sqlite3

# Connect to the database file
conn = sqlite3.connect("scores.db")
cursor = conn.cursor()

# Drop existing tables if they exist (common during development)
cursor.execute("DROP TABLE IF EXISTS scores")
cursor.execute("DROP TABLE IF EXISTS players")

# Create players table
cursor.execute("""
    CREATE TABLE players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
""")

# Create scores table with foreign key
cursor.execute("""
    CREATE TABLE scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_id INTEGER,
        score INTEGER,
        date TEXT,
        FOREIGN KEY (player_id) REFERENCES players(id)
    )
""")

# Insert test players
players = [("Alice",), ("Bob",), ("Charlie",)]
cursor.executemany("INSERT INTO players (name) VALUES (?)", players)

# Insert test scores
scores = [
    (1, 120, '2025-05-01'),
    (1, 100, '2025-05-03'),
    (2, 90,  '2025-05-02'),
    (3, 110, '2025-05-01'),
    (2, 150, '2025-05-05')
]
cursor.executemany("INSERT INTO scores (player_id, score, date) VALUES (?, ?, ?)", scores)

# Commit and close connection
conn.commit()
conn.close()

print("Database and test data created successfully!")