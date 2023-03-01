from dbConnect import *
from time import sleep


def viewDirector():
    cursor.execute("SELECT Title, Director FROM Films")
    genreQuery = cursor.fetchall()

    if genreQuery == []:
        print("The database is empty.")
        sleep(2)
        return 0
    else:
        print("\nDirector List:")
        for record in genreQuery:
            print(record)
        return 1


if __name__ == "__main__":
    viewDirector()
