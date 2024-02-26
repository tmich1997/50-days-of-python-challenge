# Day 49: Create a Database

import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS movies (
               year INTEGER,
               title TEXT,
               genre TEXT
        )
''')

movies_data = [
    (2009, 'Brothers', 'Drama'),
    (2002, 'Spider Man', 'Sci-fi'),
    (2009, 'WatchMen', 'Drama'),
    (2010, 'Inception', 'Sci-fi'),
    (2009, 'Avatar', 'Fantasy')
]

cursor.executemany(
        "INSERT INTO movies (year, title, genre) VALUES (?, ?, ?)", movies_data
)

connection.commit()

connection.close()

print("Table CREATED and Data INSERTED")

connection_1 = sqlite3.connect('movies.db')

cursor_1 = connection_1.cursor()

# a) Once you create a table, run a SQL query to see all the movies in your table.

cursor_1.execute(
    """
    SELECT *
    FROM movies

    """
)

rows = cursor_1.fetchall()

for row in rows:
    print(row)

# b) Run another SQL query to select only the movie Brothers from the list.
    
cursor_1.execute(
    """
    SELECT *
    FROM movies
    WHERE title == 'Brothers'

    """
)

rows = cursor_1.fetchall()

for row in rows:
    print(row)

# c) Run another SQL query to select all movies that were released in 2009 from your table.
    
cursor_1.execute(
    """
    SELECT *
    FROM movies
    WHERE year == 2009

    """
)

rows = cursor_1.fetchall()

for row in rows:
    print(row)

# d) Run another query to select movies in the fantasy and drama genres.
    
cursor_1.execute(
    """
    SELECT *
    FROM movies
    WHERE genre = 'Fantasy' or genre = 'Drama'

    """
)

rows = cursor_1.fetchall()

for row in rows:
    print(row)

# e) Run a query to delete all the contents of your table.
    
cursor_1.execute(
    """
    DELETE FROM movies

    """
)

connection_1.commit()

connection_1.close()

print("Content deleted")