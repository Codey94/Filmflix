from dbConnect import *
from time import sleep


def viewRatings():
    cursor.execute("SELECT Title, Rating FROM Films")
    ratingQuery = cursor.fetchall()

    if ratingQuery == []:
        print("The database is empty.")
        sleep(2)
        return 0
    else:
        print("\nRatings List:")
        for record in ratingQuery:
            print(record)
        return 1


if __name__ == "__main__":
    viewRatings()
