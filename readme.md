## Overview

**Project Title**:
Game Score Tracker - Cloud Edition
**Project Description**:
This version of the Game Score Tracker integrates cloud database support using Google Firestore. The web-based interface allows users to add, view, update, and delete game scores, which are stored remotely in Firestore. This demonstrates an upgrade from local SQLite storage to a fully cloud-enabled application, showcasing how to use Python and Firebase to manage game data online.

**Project Goals**:
- Connect the existing game score tracker to a Firestore cloud database
- Learn Firestore and firebase-admin integration in Python
- Implement full CRUD operations (Create, Read, Update, Delete) via cloud API
- Build a simple and responsive front-end using HTML and JavaScript
- Implement real-time updates for score data using Firestore listeners

## Instructions for Build and Use

1. Clone the repository or download the source files
2. Set up the Python virtual environment:  
   `python3 -m venv .venv && source .venv/bin/activate`
3. Install required dependencies:  
   `pip install flask firebase-admin`
4. Place your Firebase service account JSON file in the root directory
5. Ensure `serviceAccountKey.json` matches your Firebase credentials
6. Run the Flask app:
   `python app.py`
7. Open `http://127.0.0.1:5000` in a browser to access the web interface

Usage:
- Add a player name and score through the input form
- Click "Submit" to store the score in Firestore
- Use the Edit/Delete buttons next to each record to update or remove data

## Development Environment 

* Python 3.10+
* Flask
* firebase-admin
* Google Firebase / Firestore
* VS Code (recommended)

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [W3Schools SQL Tutorial](https://www.w3schools.com/sql/default.asp)
* [Introducing SQL and Relational Databases (O'Reilly)](https://learning.oreilly.com/course/introducing-sql-and/9781484238417/)
* [SQLite Python Tutorial](https://www.sqlitetutorial.net/sqlite-python/)

## Sprint 3 Cloud Database Integration

During Sprint 3, the Game Score Tracker was extended to use Google Firestore as a cloud backend. The previous local SQLite implementation was replaced with cloud-based storage. The Flask web server allows users to interact with the database via a browser, and Firebase’s real-time database features allow data to sync and update live. All required CRUD operations were implemented using Firestore API through `firebase-admin`. A stretch goal of real-time data listening and live updates was also achieved using Firestore's `onSnapshot()` functionality in the front-end.

## Future Work

* [ ] Add user authentication with Firebase
* [ ] Improve responsive design and UI/UX
* [ ] Add multiple collections for better data separation (e.g. users, scores)
