import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("vector_database.db")
cursor = conn.cursor()

#cursor.execute('CREATE TABLE IF NOT EXISTS vector_table ( id INTEGER PRIMARY KEY,  vector_data TEXT)')

# Assume 'vectors' is a list of vectors
vectors = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]

# Convert vectors to string format
vector_strings = [",".join(map(str, vector)) for vector in vectors]

# Insert vectors into the table
for vector_string in vector_strings:
    cursor.execute('INSERT INTO vector_table (vector_data) VALUES (?)', (vector_string,))

# Commit the changes
conn.commit()

# Fetch all vectors from the table
cursor.execute('SELECT id, vector_data FROM vector_table')
rows = cursor.fetchall()

# Convert fetched vectors to a list of lists or arrays
stored_vectors = [list(map(float, row[1].split(','))) for row in rows]

print(stored_vectors)

# Close the connection
conn.close()
