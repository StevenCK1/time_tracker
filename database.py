import typer
import sqlite3
from tabulate import tabulate

# Creating app object
app = typer.Typer()
# Connect to database
con = sqlite3.connect("timeTracker.db")

# Create a cursor
cur = con.cursor()

# CLI command to create table
@app.command()
def createTable():
    # Create a table (using six double quote since it give me multi-line view of the code)
    cur.execute("""CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    message TEXT,
    status TEXT,
    started_at TEXT,
    stopped_at TEXT
)""")

# CLI command to list all entries
@app.command()
def list():
    cur.execute("SELECT * FROM tasks")
    results = cur.fetchall()
    print(tabulate(results, headers=["ID","Message", "Status", "Started at", "Stopped at"], tablefmt="fancy_grid"))

# CLI command to create new entry
@app.command()
def create(message: str):
    cur.execute(f"INSERT INTO tasks (message, status, started_at, stopped_at) VALUES ('{message}', 'running', datetime('now', 'localtime'), 'Not stopped yet')")

    # re-list all entries after new entry creation
    cur.execute("SELECT * FROM tasks")
    results = cur.fetchall()
    print(results, headers=["ID","Message", "Status", "Started at", "Stopped at"], tablefmt="fancy_grid")
    # Commit command
    con.commit()
    

# Close connection, commented out since was getting error "sqlite3.ProgrammingError: Cannot operate on a closed database."
# con.close()

# Calling app object
if __name__ == "__main__": 
    app()