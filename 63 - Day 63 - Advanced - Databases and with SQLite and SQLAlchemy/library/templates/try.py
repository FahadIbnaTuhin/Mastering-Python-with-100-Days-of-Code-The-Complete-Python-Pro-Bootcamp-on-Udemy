import sqlite3

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

# cursor.execute("CREATE TABLE MOVIE(title, year, score)")
# res = cursor.execute("SELECT title FROM MOVIE")
# call res.fetchone() to fetch the resulting row:
# if res.fetchone() is None:
#     print("TRUE")

# cursor.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)

res = cursor.execute("SELECT * FROM MOVIE")
#  call res.fetchall() to return all resulting rows:
print(res.fetchall())







