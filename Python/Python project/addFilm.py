from dbConnect import *
from time import sleep


def insertFilm():
    film = []
    title = input("Please enter the movie name: ")
    director = input("Please enter the directors name: ")
    genre = input("Please enter the genre of the movie: ")

    film.append(title)
    film.append(director)
    film.append(genre)

    print(film)

    addSql = f"""
	INSERT INTO Films VALUES (NULL, "{film[0]}", "{film[1]}", "{film[2]}")
	"""

    cursor.execute(addSql)
    conn.commit()

    print(f"{title} has been successfully added to the database.")
    sleep(3)


if __name__ == "__main__":
    insertFilm()
