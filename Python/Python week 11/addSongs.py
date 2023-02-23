from connect import *
from time import sleep
from readSongs import read
# Inserting values into a table


def insertSongs():
    song = []
    title = input("Enter a name of a song: ")
    artist = input("Enter the artist's Name: ")
    genre = input("Enter the genre of the song: ")

    song.append(title)
    song.append(artist)
    song.append(genre)

    print(song)

    sqlCode = f"""
	INSERT INTO songs VALUES (NULL, "{song[0]}", "{song[1]}", "{song[2]}")
	"""

    cursor.execute(sqlCode)
    conn.commit()

    print(f"{title} has been successfully added to the database.")
    sleep(3)
    read()


if __name__ == "__main__":
    insertSongs()
