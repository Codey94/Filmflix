# Connecting to a database with SQLite

import sqlite3 as sql

# Connect/Initialize the database

conn = sql.connect(r"Python\Python project\bootcamp.db")


# Execute SQL commands, by accessing the cursor, then executing commands.
# conn.cursor().execute("SELECT * FROM tablename")


# Simplify executing SQL code, by storing the cursor in a variable
cursor = conn.cursor()


# Now we can execute SQL code:
# cursor.execute(mysql code in here)
# cursor.execute()
# CRUD Operation (Create, Read, Update, Delete)
