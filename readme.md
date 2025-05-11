## Overview

**Project Title**:
Game Score Tracker CLI Tool
**Project Description**:
This project is a command-line interface (CLI) tool written in Python that manages player score data using a local SQLite database. It allows users to add, update, delete, and query scores. The system uses two tables: players and scores, connected by a foreign key. This project was completed as part of an Applied Programming module, and it demonstrates core database operations using SQL through Python’s built-in sqlite3 library.

**Project Goals**:
- Learn the basics of SQL and relational databases
- Practice Python-SQLite integration
- Complete full CRUD (Create, Read, Update, Delete) operations
- Build a working CLI for player score management
- Complete a stretch challenge using a date-based query filter

## Instructions for Build and Use

Steps to build and/or run the software:

1. Clone the repository or download the source files
2. Set up the Python virtual environment:  
   `python3 -m venv .venv && source .venv/bin/activate`
3. Install any necessary dependencies (only `sqlite3`, which is built-in)


Instructions for using the software:

1. Run `db_setup.py` to initialize tables and insert test data:  
   `python db_setup.py`
2. Use `cli.py` to interact with the system:
   - Add player: `python cli.py add-player "Alice"`
   - Add score: `python cli.py add-score 1 120 2025-05-01`
   - List scores: `python cli.py list-scores`
   - Update score: `python cli.py update-score 1 150`
   - Delete score: `python cli.py delete-score 2`


## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python 3.10+
* SQLite (included with Python)
* VS Code (optional but recommended)

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [W3Schools SQL Tutorial](https://www.w3schools.com/sql/default.asp)
* [Introducing SQL and Relational Databases (O'Reilly)](https://learning.oreilly.com/course/introducing-sql-and/9781484238417/)
* [SQLite Python Tutorial](https://www.sqlitetutorial.net/sqlite-python/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add error handling and input validation
* [ ] Use argparse mutually exclusive groups for better CLI UX
* [ ] Export scores to CSV
