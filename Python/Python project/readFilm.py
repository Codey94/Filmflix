from dbConnect import *
from time import sleep


def read():
    cursor.execute("SELECT * FROM Films")
    query = cursor.fetchall()

    if query == []:
        print("The database is empty.")
        sleep(2)
        return 0
    else:
        print("\nMovie List:")
        for record in query:
            print(record)
        return 1


if __name__ == "__main__":
    read()
