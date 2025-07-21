## Overview

**Project Title**:
Game Score Tracker - Networking Edition
**Project Description**:
This version of the Game Score Tracker extends the original CLI tool by adding client-server networking capabilities using Python sockets. The client sends requests to the server to add players, add scores, and list existing records. The server interacts with a local SQLite database and handles JSON-formatted communication. This project demonstrates a transition from a single-user CLI to a networked multi-client backend architecture.

**Project Goals**:
- Extend previous CLI app with TCP-based client-server communication
- Learn socket programming fundamentals in Python
- Build a server to handle multiple types of client requests
- Parse and respond with JSON over a network socket
- Integrate database read/write logic with network communication

## Instructions for Build and Use

Steps to build and/or run the software:

1. Clone the repository or download the source files
2. Set up the Python virtual environment:  
   `python3 -m venv .venv && source .venv/bin/activate`
3. Install any necessary dependencies (only `sqlite3`, which is built-in)
4. To run the server:
   `python server.py`
5. To run the client:
   `python client.py`

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
* Flask (for optional web frontend)
* Python socket (for networking features)

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [W3Schools SQL Tutorial](https://www.w3schools.com/sql/default.asp)
* [Introducing SQL and Relational Databases (O'Reilly)](https://learning.oreilly.com/course/introducing-sql-and/9781484238417/)
* [SQLite Python Tutorial](https://www.sqlitetutorial.net/sqlite-python/)

## Future Work

* [ ] Add user input validation and error feedback in client
* [ ] Improve server routing and support multiple request types
* [ ] Add a web-based interface using Flask

## Sprint 2 Networking Enhancements

During Sprint 2, the project was extended to implement a basic networking model using Python sockets. A client program was built to send commands like "add-player", "add-score", and "list-scores" in JSON format. The server receives, parses, and responds to these requests using the SQLite database created in Sprint 1. Additionally, a basic Flask app was added to serve as an optional front-end to visualize scores through a browser. This Sprint also included error handling, socket disconnection logic, and testing with multiple simulated clients.
