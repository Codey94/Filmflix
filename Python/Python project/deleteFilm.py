from readFilm import read
from dbConnect import *
from time import sleep


def delete():
    if read() == 0:
        print("There is nothing to delete")
        return
    else:
        sleep(1)
        sure = False
        while sure == False:
            filmID = input("Enter the film ID you would like to delete: ")
            confirm = input(
                f"Are you sure you would like to delete {filmID}: ")
            if confirm == "Y" or confirm == "yes" or confirm == "Yes" or confirm == "y":
                sure = True

        deleteSQL = f"DELETE FROM Films WHERE filmID = {filmID}"
        cursor.execute(deleteSQL)
        conn.commit()

        print(f"The song of ID {filmID} has been deleted.")
        sleep(2.5)
        read()


if __name__ == "__main__":
    delete()
