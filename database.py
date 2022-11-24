import sqlite3
import typer

# Creating and calling object
app = typer.Typer()

if __name__ == "__database__": 
    app()

# Connect to database
con = sqlite3.connect("timeTracker.db")

# Create a cursor
cur = con.cursor()

# Create a table (using six double quote since it give me multi-line view of the code)
cur.execute("""CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    message TEXT,
    status TEXT,
    started_at TEXT,
    stopped_at TEXT
)""")

# Commit command
con.commit()

# Close connection
con.close()