# time_tracker

First experience using python to create a database using SQLite3

Packages use:

- Typer is a library for building CLI applications
- Tabulate is a library and Command line utility tool to print tabular data in Python

Note: Sqlite3 is not in the requirement.txt file since it is included in the standard python library since Python 2.5

## Setup

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 database.py --help
```

## Run database.py to create table

```
python3 database.py createtable
```

## Run database.py to list all entries

```
python3 database.py list
```
