from connect import *
from readSongs import read
from time import sleep

def delete():
	if read() == 0:
		print("Theres nothing to delete.")
		return
	else:
		sleep(0.5)
		sure = False
		while sure == False:
			songID = input("Please enter the ID of the song you'd like to delete: ")
			confirm = input("Are you actually sure that you really want to delete this song?!!?\n(Y/N): ")
			if confirm == "Y" or confirm == "yes" or confirm == "y":
				sure = True

		deleteSQL = f"DELETE FROM songs WHERE SongID = {songID}"
		cursor.execute(deleteSQL)
		conn.commit()

		print(f"The song of ID {songID} has been deleted.")
		sleep(2.5)
		read()

if __name__ == "__main__":
	delete()