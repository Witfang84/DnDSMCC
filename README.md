# DnD Story Mode Character Creator

This project provides a minimal Flask web app for creating and managing Dungeons & Dragons characters using the "Story Mode" ruleset.

## Installation

1. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

Start the development server with:

```bash
python src/app.py
```

Then open `http://localhost:5000` in your browser.

## Project Structure

- `src/app.py` – Flask application with routes and controllers
- `src/templates/` – HTML templates for the user interface
- `requirements.txt` – Python dependencies

Characters are stored in memory, so restarting the server clears them. This project is intended as a starting point for further development.
