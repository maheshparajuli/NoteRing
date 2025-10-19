import sqlite3
from datetime import datetime

# click is a Python package used to create command-line interface (CLI) commands.
import click
from flask import current_app,g

""" 
1. The detect_types=sqlite3.PARSE_DECLTYPES part tells SQLite:
“When fetching rows, automatically convert columns into their proper Python types
 based on how they were declared in the table (like DATE, TIMESTAMP, etc.).”


2. g.db.row_factory = sqlite3.Row
By default, fetching from SQLite gives you tuples, like (1, 'Mahesh').
Setting .row_factory = sqlite3.Row makes rows act like dict-like objects, so you can access columns by name:

3. In Flask, g (short for “global”) is a special object used to store data during a single request.

4. sqlite3.Row is a special class built into Python's sqlite3 module that makes rows act 
like dictionaries, i.e., you can access values by column name.

"""

def get_db():
    if 'db' not in g:
        g.db=sqlite3.connect(current_app.config['DATABASE'],detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory=sqlite3.Row
    return g.db

def close_db(e=None):
    
    db=g.pop('db',None)

    if db is not None:
        db.close()


# The executescript() method specifically requires a string, not a file object. So you can't skip f.read().
# sqlite3.register_converter(typename, callable)






