from dbConnect import *
from time import sleep


def viewYears():
    cursor.execute("SELECT Title, Year FROM Films")
    titleQuery = cursor.fetchall()

    if titleQuery == []:
        print("The database is empty.")
        sleep(2)
        return 0
    else:
        print("\nYear List:")
        for record in titleQuery:
            print(record)
        return 1


if __name__ == "__main__":
    viewYears()
