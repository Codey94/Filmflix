from dbConnect import *
from time import sleep
from readFilm import read


def update():
    if read() == 0:
        print("There are no films to update at this time.")
        return
    else:
        filmID = input("Enter the ID of the movie you would like to update:")

        title = input("Enter the new title of the movie:")
        director = input("Enter the new director of the movie:")
        genre = input("Enter the new genre of the movie:")
        year = input("Enter the new year of the movie")
        rating = input("Enter the new rating from 1 - 5")

        updateSQL = f"""
        UPDATE Films
        SET Title = "{title}", Director = "{director}", Genre = "{genre}", Year = "{year}", Rating = "{rating}"
        WHERE filmID = {filmID};
        
        """
        cursor.execute(updateSQL)
        conn.commit()
        print(f"film ID: {filmID} has been successfully updated.")
        sleep(3)


if __name__ == "__main__":
    update()
