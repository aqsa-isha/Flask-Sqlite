import sqlite3

# Connect to the database (it will create the database if it doesn't exist)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create the students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    addr TEXT NOT NULL,
    city TEXT NOT NULL,
    pin TEXT NOT NULL
)
''')

# Commit and close the connection
conn.commit()
conn.close()


print("Table 'students' created successfully.")
